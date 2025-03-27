from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

Username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "firstName"))
)
Lastname = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "lastName"))
)
Email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "userEmail"))
)
Gender = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "gender-radio-1"))
)
Mobile = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "userNumber"))
)
submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit"))
)


Username.send_keys("Andres")
Lastname.send_keys("Quintero")
Email.send_keys("Andresmail@gmail.com")

Gender = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[@for='gender-radio-3']"))
)
Gender.click()

Mobile.send_keys("9514782001")
driver.execute_script("arguments[0].scrollIntoView();", submit)  # Hacer scroll
submit.click()


Thanks = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg")))
Palabra = Thanks.text
assert "Thanks" in Palabra, "La palabra 'Thanks' no esta en la segunda pagina"


time.sleep(4)
driver.quit()
