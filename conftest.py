import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import email_valid, password_valid


@pytest.fixture(autouse=True)
def driverChrome():
    pytest.driver = webdriver.Chrome('/Users/inescence/PycharmProjects/pythonProject/selenium/chromedriver')
    pytest.driver.implicitly_wait(10)
    pytest.driver.maximize_window()
    pytest.driver.get('https://b2c.passport.rt.ru/')
    yield driverChrome
    pytest.driver.quit()


@pytest.fixture()
def go_to_forgot_password_page():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'username').send_keys(email_valid)
    pytest.driver.find_element(By.ID, 'password').send_keys(password_valid)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'forgot_password')))
    pytest.driver.find_element(By.ID, 'forgot_password').click()


@pytest.fixture()
def go_to_register_page():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'kc-register').click()