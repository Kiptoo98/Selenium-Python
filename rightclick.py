from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com/')

value = driver.find_element(By.CLASS_NAME, "gb_5")

action = ActionChains(driver)

action.context_click(value).perform()