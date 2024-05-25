from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
button_name = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(button_name)


