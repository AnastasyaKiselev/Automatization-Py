from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Login3 import Login3
from MainPage3 import Main3
from CartCheckout3 import CartCheckout3
from TotalLabel3 import TotalLabel3

def test_total_score3():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login = Login3(driver)
    login.LoginPage3()
    main = Main3(driver)
    main.MainPage()
    cart_chekcout = CartCheckout3(driver)
    cart_chekcout.Cart()
    cart_chekcout.CheckoutInfo()
    total = TotalLabel3(driver)
    total.TotalLabel()