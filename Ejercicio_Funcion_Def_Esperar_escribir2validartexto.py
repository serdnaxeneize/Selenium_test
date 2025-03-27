from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()


def encontrar_elemento(driver, locator, tiempo=3):
    return WebDriverWait(driver, tiempo).until(EC.presence_of_element_located(locator))


def escribir_elemento(driver, locator, texto, tiempo=3):
    elemento = encontrar_elemento(driver, locator, tiempo)
    elemento.send_keys(texto)
    valor_ingresado = elemento.get_attribute("value")
    print(f"✅ Se ingresó '{valor_ingresado}' en el campo {locator}")
    return valor_ingresado


Nombre = escribir_elemento(driver, (By.ID, 'firstName'), 'Andres')
print(f'✅ El nombre ingresado es:{Nombre}')

Apellido = escribir_elemento(driver, (By.ID, 'lastName'), 'Andres')
print(f'✅ El apellido ingresado es:{Apellido}')

Correo = escribir_elemento(driver, (By.ID, 'userEmail'), 'Andres@hotmail.com')
print(f'✅ El correo ingresado es:{Correo}')

Telefono = escribir_elemento(driver, (By.ID, 'userNumber'), '1234567890')
print(f'✅ El telefono ingresado es:{Telefono}')


driver.quit()
