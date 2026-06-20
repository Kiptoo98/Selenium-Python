from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://www.ebay.com/')

value = driver.find_element(By.XPATH, '//*[@id="gh"]/nav/div[2]/div[4]/a/span')

action = ActionChains(driver)

action.move_to_element(value).perform()