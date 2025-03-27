from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()


# Aquí defino la funcion
def esperar_elemento(driver, locator, tiempo):
    return WebDriverWait(driver, tiempo).until(EC.presence_of_element_located(locator))


def escribir_elemento(driver, locator, text, tiempo=3):
    elemento = esperar_elemento(driver, tiempo).until(
        EC.presence_of_element_located(locator))
    elemento.send_keys(text)
    return elemento  # Devuelve el elemento para validar después


# Aqui llamo la funcion esperar elemento
Nombre = esperar_elemento(driver, (By.ID, 'firstName'), 6)

# Aqui llamo la funcion escribir elemento
Nombre = escribir_elemento(driver, (By.ID, 'firstName'), 'Andres Felipe', 5)
Apellido = escribir_elemento(driver, (By.ID, 'lastName'), 'Quintero', 5)

if Nombre:
    print('✅ El nombre fue diligenciado')

if Apellido:
    print('✅ El apellido fue diligenciado')


driver.quit()
