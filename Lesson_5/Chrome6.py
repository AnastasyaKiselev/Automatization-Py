from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

login_input = driver.find_element(By.CSS_SELECTOR, '#username')
login_input.send_keys('tomsmith', Keys.RETURN)

password_input = driver.find_element(By.CSS_SELECTOR, '#password')
password_input.send_keys('SuperSecretPassword!', Keys.RETURN)
button_login = driver.find_element(By.CSS_SELECTOR, '.radius').click()
sleep(9)
