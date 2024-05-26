from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

cookie = {
    'name': 'cookie_policy',
    'value': '1'
}


def test_card():
    list=[]
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://labirint.ru")
    driver.implicitly_wait(4)
    driver.add_cookie(cookie)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys("Python", Keys.RETURN)
    list = driver.find_elements(By.CSS_SELECTOR, "._btn.btn-tocart.buy-link")
    counter = 0
    for i in list:
        i.click()
        counter+=1
    sleep(4)
    print("Число кликов = ", counter)



    driver.quit()

test_card()