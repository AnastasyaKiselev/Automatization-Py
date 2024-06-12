from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Main2 import Main2

def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main=Main2(driver)
    main.start_testing(driver)
    main.set_time(45)
    main.clicking()
    main.waiting_result()




