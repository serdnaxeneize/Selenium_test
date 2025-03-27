from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service()
driver = webdriver.Edge(service=service)

driver.get("https://duckduckgo.com/")
time.sleep(2)

Buscar = driver.find_element(By.NAME, "q")

Botn = driver.find_element(
    By.XPATH, ('//*[@id="searchbox_homepage"]/div/div/div/button'))
time.sleep(2)


Buscar.send_keys("Python Automation")
Botn.click()
time.sleep(2)

Buscar = driver.find_element(By.NAME, "q")
Palabra = Buscar.get_attribute("value")
assert Palabra == "Python Automation"


# Verificar que la pagina cargó correctamente
titulo = driver.title
print(f"El titulo de la pagina es "+titulo)
assert "Automation" in titulo, "La pagina de resultados no se cargó correctamente"


# Obtener el texto del primer resultado usando un XPath relativo
PrimerResultado = driver.find_element(
    By.XPATH, ('//h2/a/span'))
TextoResultado = PrimerResultado.text

print(f"El primer resulado es: {TextoResultado}")


# Validar que el título del primer resultado contiene la palabra "Python"
assert "Python" in TextoResultado, "El texto no fue encontrado en el primer resultado"
time.sleep(2)

driver.quit()
