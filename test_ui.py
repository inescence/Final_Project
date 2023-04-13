import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from settings import email_valid, password_valid


# 1. стартовая страница открывается, обязательные элементы присутствуют
def test_page_loading_correctly():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "kc-login")))


# 2. При вводе неверного пароля цвет ссылки "забыл пароль" меняется на оранжевый
def test_forgot_password_changes_colour():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'username').send_keys(email_valid)
    pytest.driver.find_element(By.ID, 'password').send_keys(password_valid)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button['
                                                                                            'type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'forgot_password')))
    btn_colour = pytest.driver.find_element(By.ID, 'forgot_password').value_of_css_property(
        'color')
    assert btn_colour == 'rgba(255, 79, 18, 1.0)'


# 3. Ссылка "Забыл пароль" ведёт на страницу восстановления пароля
def test_forgot_passport_link_redirection_correct():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').get_attribute("innerHTML") == 'Восстановление пароля'


# 4. На странице восстановления пароля присутствуют все необходимые поля.
def test_forgot_password_page_loading_correctly(go_to_forgot_password_page):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "captcha")))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "rt-captcha__image")))


# 5. На странице восстановления обновляется капча.
def test_captcha_updates_correctly(go_to_forgot_password_page):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    captcha1 = pytest.driver.find_element(By.CLASS_NAME, 'rt-captcha__image').get_attribute("src")
    pytest.driver.find_element(By.CLASS_NAME, 'rt-captcha__reload-con').click()
    captcha2 = pytest.driver.find_element(By.CLASS_NAME, 'rt-captcha__image').get_attribute("src")
    assert captcha1 != captcha2


# 6. Ссылка на пользовательское соглашение в блоке авторизации работает
def test_terms_of_use_left_block_link_works():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'app-footer')))
    pytest.driver.find_element(By.LINK_TEXT, 'пользовательского соглашения').click()
    pytest.driver.switch_to.window(pytest.driver.window_handles[1])
    url = pytest.driver.current_url
    assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'


# 7. Ссылка на политику конфиденциальности и пользовательское соглашение в футере работает
def test_privacy_policy_footer_link_works():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'app-footer')))
    pytest.driver.find_element(By.ID, 'rt-footer-agreement-link').click()
    pytest.driver.switch_to.window(pytest.driver.window_handles[1])
    url = pytest.driver.current_url
    assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'


# 8. Ссылка Cookies в футере открывает окно с подсказкой
def test_footer_cookies_popup_works():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'app-footer')))
    pytest.driver.find_element(By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]/span/span').click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "rt-cookies-tip")))

