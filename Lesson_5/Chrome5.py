
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")

number_input = driver.find_element(By.CSS_SELECTOR, '[type="number"]')

number_input.send_keys('1000', Keys.RETURN)
sleep(1)
number_input.clear()
sleep(1)
number_input.send_keys('999', Keys.RETURN)
sleep(3)