import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import *


# 1. ссылка на страницу регистрации в блоке авторизации работает
def test_register_link_redirection():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'kc-register').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert title == 'Регистрация'


# 2. позитивный тест на регистрацию
def test_register_positive(go_to_register_page):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(first_name_valid)
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(last_name_valid)
    pytest.driver.find_element(By.ID, 'address').send_keys('abc@asda.ru')
    pytest.driver.find_element(By.ID, 'password').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.NAME, 'register').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').text
    assert title == 'Подтверждение email'


# 3. негативный тест на регистрацию с невалидными именем/фамилией
@pytest.mark.parametrize('first_name', first_name_invalid)
@pytest.mark.parametrize('last_name', last_name_invalid)
def test_register_invalid_first_and_last_name(go_to_register_page, first_name, last_name):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(first_name)
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(last_name)
    pytest.driver.find_element(By.ID, 'address').send_keys('abc@asdad.ru')
    pytest.driver.find_element(By.ID, 'password').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.NAME, 'register').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').text
    assert title == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 4. негативные тесты на регистрацию по неверному телефону
@pytest.mark.parametrize('phone', phone_invalid)
def test_register_invalid_email(go_to_register_page, phone):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(first_name_valid)
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(last_name_valid)
    pytest.driver.find_element(By.ID, 'address').send_keys(phone)
    pytest.driver.find_element(By.ID, 'password').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.NAME, 'register').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').text
    assert title == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


# 5. негативные тесты на регистрацию по неверному email
@pytest.mark.parametrize('email', email_invalid)
def test_register_invalid_phone(go_to_register_page, email):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(first_name_valid)
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(last_name_valid)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.NAME, 'register').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta--error').text
    assert title == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


# 6. негативный тест на регистрацию по уже существующему телефону
@pytest.mark.parametrize('phone', phone_taken)
def test_register_phone_already_in_use(go_to_register_page, phone):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(first_name_valid)
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(last_name_valid)
    pytest.driver.find_element(By.ID, 'address').send_keys(phone)
    pytest.driver.find_element(By.ID, 'password').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.NAME, 'register').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-modal__title').text
    assert title == 'Учётная запись уже существует'


# 7. негативный тест на регистрацию по уже существующему email
@pytest.mark.parametrize('email', email_valid)
def test_register_email_already_in_use(go_to_register_page, email):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-container__title")))
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(first_name_valid)
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(last_name_valid)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Qq123456789Qq')
    pytest.driver.find_element(By.NAME, 'register').click()
    title = pytest.driver.find_element(By.CLASS_NAME, 'card-modal__title').text
    assert title == 'Учётная запись уже существует'

