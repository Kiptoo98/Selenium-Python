from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://demoqa.com/alerts')

driver.find_element(By.ID, 'alertButton').click()

alert = driver.switch_to.alert
print("Popup text: ", alert.text)
alert.accept()
print("Alert accepted")