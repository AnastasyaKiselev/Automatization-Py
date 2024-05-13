from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)
modal = driver.find_element(By.CSS_SELECTOR, '#modal')
button = modal.find_element(By.CLASS_NAME, 'modal-footer').click()

sleep(5)

