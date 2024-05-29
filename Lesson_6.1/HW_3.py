from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import re
def test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click() 
    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Nastya")
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Kiseleva")
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('197348')
    driver.find_element(By.CSS_SELECTOR, '#continue').click() 
    total_label = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    price = total_label.split("$")[1]
    print (price)
    assert  price == '58.29'


