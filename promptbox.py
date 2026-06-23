from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://demoqa.com/alerts')

driver.find_element(By.ID, "promtButton").click()

prompt = driver.switch_to.alert
prompt.send_keys("Brian Kiptoo")
prompt.accept()