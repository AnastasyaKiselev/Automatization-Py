from selenium.webdriver.common.by import By
class Main3:
    def __init__(self, driver):
        self._driver = driver

    def MainPage(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        self._driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]').click()