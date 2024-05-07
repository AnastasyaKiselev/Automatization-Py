from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(" http://the-internet.herokuapp.com/add_remove_elements/")


button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()
button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()
button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()
button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()
button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()

count = []

value = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
for e in value:
    print(e.text)
    count.append(e.text)


print(count)    
print (len(count))