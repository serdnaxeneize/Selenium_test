from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Creo la funcion de encontrar elementos


def encontrar_elemento(driver, locator, tiempo=5):
    return WebDriverWait(driver, tiempo).until(EC.presence_of_element_located(locator))

# Creo la funcion de escribir sobre elemento


def escribir_elemento(driver, locator, texto, tiempo=3):
    elemento = encontrar_elemento(driver, locator, tiempo)
    elemento.send_keys(texto)
    return elemento


# Llamó la función para diferentes campos
Nombre = escribir_elemento(driver, (By.ID, 'firstName'), 'Andres')
print('✅ El nombre fue diligenciado')
Apellido = escribir_elemento(driver, (By.ID, 'lastName'), 'Quintero')
print('✅ El apellido fue diligenciado')
Correo = escribir_elemento(
    driver, (By.ID, 'userEmail'), 'andresquintero1@gmail.com')
print('✅ El correo fue diligenciado')
Numero_telefono = escribir_elemento(
    driver, (By.ID, 'userNumber'), '1234567890')
print('✅ El numero fue diligenciado')


driver.quit()
