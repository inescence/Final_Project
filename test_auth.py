import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import *


# 1. позитивный тест на авторизацию по телефону
@pytest.mark.parametrize('phone', phone_valid)
def test_phone_auth_positive(phone, password=password_valid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(phone)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "main-header-menu__logout")))


# 2. негативный тест на авторизацию по телефону
@pytest.mark.parametrize('phone', phone_invalid)
def test_phone_auth_negative(phone, password=password_valid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(phone)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert title == 'Авторизация'


# 3. позитивный тест на авторизацию по почте
def test_email_auth_positive(email=email_valid, password=password_valid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "main-header-menu__logout")))


# 4. негативный тест на авторизацию по почте
@pytest.mark.parametrize('email', email_invalid)
def test_phone_auth_negative(email, password=password_valid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert title == 'Авторизация'


# 5. позитивный тест на авторизацию по логину
def test_login_auth_positive(login=login_valid, password=password_valid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(login)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "main-header-menu__logout")))


# 6. негативный тест на авторизацию по логину
@pytest.mark.parametrize('login', login_invalid)
def test_login_auth_negative(login, password=password_valid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(login)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert title == 'Авторизация'


# 7. позитивный тест на авторизацию по лицевому счету
def test_personal_account_auth_positive(p_acc=personal_account_valid, password=password_valid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(p_acc)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "main-header-menu__logout")))


# 8. негативный тест на авторизацию по лицевому счету
@pytest.mark.parametrize('p_acc', personal_account_invalid)
def test_personal_account_auth_negative(p_acc, password=password_valid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(p_acc)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert title == 'Авторизация'


# 10. Негативный тест с неверным паролем
def test_wrong_password_auth_negative(p_acc=personal_account_valid, password=password_invalid):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(p_acc)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert title == 'Авторизация'


# 11. Негативный тест во всеми пустыми значениями
def test_all_empty_auth_negative(p_acc='', password=''):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(p_acc)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'kc-login').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert title == 'Авторизация'


# 12. авторизация через ВКонтакте работает
def test_auth_vk_redirection():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'oidc_vk').click()
    url = pytest.driver.current_url
    assert url[0:30] == 'https://oauth.vk.com/authorize'


# 13. авторизация через Одноклассники работает
def test_auth_ok_redirection():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'oidc_ok').click()
    url = pytest.driver.current_url
    assert url[0:22] == 'https://connect.ok.ru/'


# 14. авторизация через mail.ru работает
def test_auth_mail_ru_redirection():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'oidc_mail').click()
    url = pytest.driver.current_url
    assert url[0:22] == 'https://connect.ok.ru/'


# 15. авторизация через google.com работает
def test_auth_google_redirection():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'oidc_google').click()
    url = pytest.driver.current_url
    assert url[0:36] == 'https://accounts.google.com/o/oauth2'


# 16. авторизация через ya.ru работает
def test_auth_ya_ru_redirection():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'oidc_ya').click()
    url = pytest.driver.current_url
    assert url[0:31] == 'https://passport.yandex.ru/auth'