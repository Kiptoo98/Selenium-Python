from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://demoqa.com/alerts')

driver.find_element(By.ID, 'timerAlertButton').click()

WebDriverWait(driver,5).until(EC.alert_is_present())
alert = driver.switch_to.alert
print("Popup text: ", alert.text)
alert.accept()
print("Alert accepted")