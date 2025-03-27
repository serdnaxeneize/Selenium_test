from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.gmail.com")

usuario = driver.find_element(By.ID, "identifierId")
usuario.send_keys("andresquinterof1")

btext = driver.find_element(
    By.XPATH, '//*[@id="identifierNext"]/div/button').click()
time.sleep(3)
print("Se ingresó el correo")

# Esperar hasta que el campo de contraseña esté presente
clave = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Passwd"))
)
print("Se localizó el campo clave")
clave.send_keys("Enviar clave")
print("Se envió la clave errónea")
time.sleep(7)
clave.send_keys(Keys.RETURN)

driver.quit()
