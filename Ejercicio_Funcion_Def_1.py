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


# Función para esperar un elemento

def esperar_elemento(driver, locator, tiempo=5):
    return WebDriverWait(driver, tiempo).until(EC.presence_of_element_located(locator))


# Esperar a que el botón aparezca
boton = esperar_elemento(driver, (By.ID, "submit"), 6)


# Verificar que el botón es visible
if boton:
    print("✅ Botón visible después de la espera.")

driver.quit()
