from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Form1 import Form1

def test_form_asserting():
    first_name = 'Иван'
    last_name = 'Петров'
    adress = 'Ленина, 55-3'
    email = 'test@skypro.com'
    phone = '+7985899998787'
    zipcode = ''
    city = 'Москва'
    country = 'Россия'
    job = 'QA'
    company = 'SkyPro'



    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form = Form1(driver)
    form.form_filling(first_name, last_name, adress, email, phone, zipcode, city, country, job, company)
    
        # def form_asserting(self):
    assert 'alert-danger' in driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#first-name').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#last-name').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#address').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#e-mail').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#phone').get_attribute("class")
    assert 'success' in driver.find_element(By.CSS_SELECTOR, '#city').get_attribute("class")
    