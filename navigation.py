from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/")
driver.switch_to.new_window()
driver.get("https://www.google.com/")

number_tab = len(driver.window_handles)
print(number_tab)

tab_value = driver.window_handles
print(tab_value)

current_tab = driver.current_window_handle
print(current_tab)

first_tab = tab_value[0]

if current_tab != first_tab:
    driver.switch_to.window(first_tab)

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").submit()