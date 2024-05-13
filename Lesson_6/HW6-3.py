from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiting = WebDriverWait(driver, 40)
waiting.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), 'Done!'))

third_img = driver.find_element(By.CSS_SELECTOR, '#award').get_attribute("src")
print(third_img)