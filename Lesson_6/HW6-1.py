from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(" http://uitestingplayground.com/ajax")
driver.implicitly_wait(18)


driver.find_element(By.CSS_SELECTOR, 'button#ajaxButton').click()

text_content = driver.find_element(By.CSS_SELECTOR, '#content')
content = text_content.find_element(By.CSS_SELECTOR, '.bg-success').text
print(content)