from selenium.webdriver.common.by import By

class Form1:
    def __init__(self, driver):
        self._driver = driver

    def form_filling(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys('Иван')
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys('Петров')
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys('Ленина, 55-3')
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys('test@skypro.com')
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys('+7985899998787')
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="zip-code"]').send_keys('')
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="city"]').send_keys('Москва')
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="country"]').send_keys('Россия')
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys('QA')
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys('SkyPro')
        self._driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3').click()

    def form_asserting(self):
        assert 'alert-danger' in self._driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#first-name').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#last-name').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#address').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#e-mail').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#phone').get_attribute("class")
        assert 'success' in self._driver.find_element(By.CSS_SELECTOR, '#city').get_attribute("class")
