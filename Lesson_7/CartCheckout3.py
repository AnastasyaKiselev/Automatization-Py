from selenium.webdriver.common.by import By

class CartCheckout3:
    def __init__(self, driver):
        self._driver = driver

    def Cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click() 

    def CheckoutInfo(self):
         self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Nastya")
         self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Kiseleva")
         self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('197348')
         self._driver.find_element(By.CSS_SELECTOR, '#continue').click() 
