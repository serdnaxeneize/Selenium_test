from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()


def encontrar_campos(driver, locator, tiempo=3):
    return WebDriverWait(driver, tiempo).until(EC.presence_of_element_located(locator))


def escribir_campos(driver, locator, texto, tiempo=3):
    elemento = encontrar_campos(driver, locator, tiempo)
    elemento.send_keys(texto)
    valor_ingresado = elemento.get_attribute("value")
    print(f"✅ Se ingresó '{valor_ingresado}' en el campo {locator}")
    return valor_ingresado


# Nueva función para imprimir sin repetir código
def imprimir_campo(nombre_campo, valor):
    print(f"✅ El {nombre_campo} diligenciado es: {valor}")


# Función para completar campos
Nombre = escribir_campos(driver, (By.ID, 'firstName'), 'Andres')
Apellido = escribir_campos(driver, (By.ID, 'lastName'), 'Quintero')
Correo = escribir_campos(driver, (By.ID, 'userEmail'), 'andres@gmail.com')
Telefono = escribir_campos(driver, (By.ID, 'userNumber'), '1234567890')


# Función para imprimir campos sin repetir
imprimir_campo("nombre", Nombre)
imprimir_campo("apellido", Apellido)
imprimir_campo("correo", Correo)
imprimir_campo("teléfono", Telefono)

driver.quit()
