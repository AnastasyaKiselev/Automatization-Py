from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.find_element(By.CSS_SELECTOR, '#delay').clear()
driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(45)
driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-primary' ).click()
driver.find_element(By.CSS_SELECTOR, '.operator.btn.btn-outline-success' ).click()
num = driver.find_elements(By.CSS_SELECTOR, '.btn.btn-outline-primary') #ЛОКАТОР 8!!!!!!!!
for i in num:
    if i.text =='8':
        i.click()     
driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-warning' ).click()
waiting = WebDriverWait(driver, 55).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[style='display: none;']" )))
#.spinner-border#spinner  [style="display: none;"]
