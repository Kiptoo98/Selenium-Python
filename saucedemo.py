from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome. options import Options
from selenium.webdriver.chrome. service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
options = Options()

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}

options.add_experimental_option("prefs", prefs)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.saucedemo.com/")
#driver.maximize_window()

#Entering valid username
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

#Entering valid password
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

#Clicking Submit button
driver.find_element(By.ID, "login-button").click()

#Sauce Labs Backpack - Add to cart
backpack = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
backpack.click()

#Sauce Labs Bike Light - Add to cart
bike_light = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
bike_light.click()

#Sauce Labs Bolt T-shirt - Add to cart
bolt_tshirt = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
bolt_tshirt.click()

#Sauce Labs Fleece Jacket - Add to cart
fleece_jacket = driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
fleece_jacket.click()

#Sauce Labs Onesie - Add to cart
onesie = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
onesie.click()

#Sauce Labs Red Tshirt - Add to cart
red_tshirt = driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
red_tshirt.click()

#Opening shopping cart
shopping_cart = driver.find_element(By.ID, 'shopping_cart_container')
shopping_cart.click()

#Checkout button
checkout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'checkout')))
checkout.click()

#Checkout first name
first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "first-name")))
first_name.send_keys("Tom")

#Checkout lastname
last_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "last-name")))
last_name.send_keys("Sawyer")

#Checkout postal code
postal_code = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "postal-code")))
postal_code.send_keys("00100")

#Continue button
continue_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "continue"))
)
continue_btn.click()