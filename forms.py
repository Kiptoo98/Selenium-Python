from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import os

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()

#ENTERING FIRST NAME
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("Ben")

#ENTERING LAST NAME
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Reilly")

#ENTERING EMAIL
email = driver.find_element(By.ID, "userEmail")
email.send_keys("benreilly@gmail.com")

#SELECTING MALE RADIO BUTTON
gender = driver.find_element(By.XPATH, '//*[@id="gender-radio-1"]')
gender.click()

#ENTERING MOBILE NUMBER
mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys("0723373332")

#SELECTING DATE OF BIRTH IN CALENDAR
dob = driver.find_element(By.ID, "dateOfBirthInput")

#CLICK TO OPEN CALENDAR
dob.click()

wait = WebDriverWait(driver, 10)

#SELECT YEAR
year_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__year-select')))
Select(year_dropdown).select_by_visible_text("1999")

#SELECT MONTH
month_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-datepicker__month-select')))
Select(month_dropdown).select_by_visible_text("November")

#SELECT DAY - avoid days from prev/next month
day = '1'
day_xpath = f"//div[contains(@class, 'react-datepicker__day') and text() = '{day}' and not (contains(@class, 'outside-month'))]"
wait.until(EC.element_to_be_clickable((By.XPATH, day_xpath))).click()

#ENTERING SUBJECTS
subject_input = driver.find_element(By.ID, "subjectsInput")

#ADDING SINGLE SUBJECT
# subject.click()
# subject.send_keys("ma")
# subject.send_keys(Keys.ENTER)

#ADDING MULTIPLE SUBJECTS
subjects = ["Science", "Physics", "English"]
for subject in subjects:
    subject_input.send_keys(subject)
    subject_input.send_keys(Keys.ENTER)

#SELECTING HOBBIES
driver.find_element(By.ID, "hobbies-checkbox-1").click()
driver.find_element(By.ID, "hobbies-checkbox-2").click()
driver.find_element(By.ID, "hobbies-checkbox-3").click()

#UPLOADING PICTURE
#Path to picture
img_path = os.path.abspath(r"C:\Users\bettb\OneDrive\Pictures\download (1).jpg")

#Uploading picture
image = driver.find_element(By.ID, "uploadPicture")
image.send_keys(img_path)

#CURRENT ADDRESS
address = driver.find_element(By.ID, "currentAddress")
address.send_keys("00100")

#STATE AND CITY
# Select State
state = driver.find_element(By.ID, "state")
state.click()

state_input = driver.find_element(By.ID, "react-select-3-input")
state_input.send_keys("Haryana")
state_input.send_keys(Keys.ENTER)

#Select city
city = driver.find_element(By.ID, "city")
city.click()

city_input = driver.find_element(By.ID, "react-select-4-input")
city_input.send_keys("Karnal")
city_input.send_keys(Keys.ENTER)

#SUBMIT BUTTON
submit = driver.find_element(By.ID, "submit")
submit.click()