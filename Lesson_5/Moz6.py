from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


driver = webdriver.Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")
# В поле username введите значение tomsmith
# В поле password введите значение SuperSecretPassword!
# Нажмите кнопку Login

login_input = driver.find_element(By.CSS_SELECTOR, '#username')
login_input.send_keys('tomsmith', Keys.RETURN)

password_input = driver.find_element(By.CSS_SELECTOR, '#password')
password_input.send_keys('SuperSecretPassword!', Keys.RETURN)
button_login = driver.find_element(By.CSS_SELECTOR, '.radius').click()
