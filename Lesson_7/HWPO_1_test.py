from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Form1 import Form1

def test_form_asserting():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form = Form1(driver)
    form.form_filling()
    form.form_asserting()