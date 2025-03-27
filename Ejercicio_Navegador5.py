from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://the-internet.herokuapp.com/login")


Username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'username')))

Password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'password')))

Click_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button')))

Username.send_keys("tomsmith")
Password.send_keys("SuperSecretPassword!")
Click_button.click()


# Aquí capturo el texto de la pagina, se lo asigno a una variable y luego imprimo el valor de la variable
Mensaje_Bienvenida = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'flash')))
TextoEsperado = Mensaje_Bienvenida.text

# Aqui comparo el texto esperado vs y confirmo que si esta la palabra "Secure"
assert "secure" in TextoEsperado, "El mensaje de bienvenida contiene la palabra 'secure'"
print(f"Dentro del texto completo si existe la palabra 'secure'")


# Aqui comparo Todo el texto esperado vs el texto a validar y luego imprimo
assert "You logged into a secure area!" in TextoEsperado, "El mensaje de bienvenida no es correcto"
print(f"El texto completo comparado es correcto el texto es {TextoEsperado}")

driver.quit()
