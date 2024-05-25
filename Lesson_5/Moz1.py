from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get(" http://the-internet.herokuapp.com/add_remove_elements/")

for button in range(0, 5):
    button = driver.find_element(By.CSS_SELECTOR, 'button').click()


count = []
value = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
for e in value:
    count.append(e.text)

print(count)      
print (len(count))



