from selenium.webdriver.common.by import By

class Form1:

    def __init__(self, driver):
        self._driver = driver
        
    def form_filling(self, first_name, last_name, adress, email, phone, zipcode, city, country, job, company):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys(adress)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="zip-code"]').send_keys(zipcode)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="city"]').send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="country"]').send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys(job)
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys(company)
        self._driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-primary.mt-3').click()


