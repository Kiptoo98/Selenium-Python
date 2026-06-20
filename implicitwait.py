from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.implicitly_wait(10)

username = driver.find_element(By.ID, 'user-name')
username.send_keys('standard_user')

password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')

login_btn = driver.find_element(By.ID, 'login-button')
login_btn.click()