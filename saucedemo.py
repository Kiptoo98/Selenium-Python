from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome. options import Options
from selenium.webdriver.chrome. service import Service

service = Service(executable_path="chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").submit()

driver.find_element(By.CLASS_NAME, "inventory_item_name ").click()
driver.find_element(By.ID, "add-to-cart").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "continue-shopping").click()