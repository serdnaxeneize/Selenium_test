from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://duckduckgo.com/")


Buscador = driver.find_element(By.NAME, "q")
BotonBuscador = driver.find_element(
    By.XPATH, '//*[@id="searchbox_homepage"]/div/div/div/button')


time.sleep(2)


Buscador.send_keys("Selenium WebDriver")
BotonBuscador.click()


time.sleep(2)

titulo = driver.title
print("El titulo de la pagina es "+titulo)
assert "Selenium" in titulo, "El titulo no tiene la palabra Selenium"

# Extraer texto del primer resultado de busqueda
ResultadoBusqueda = driver.find_element(
    By.XPATH, '//h2/a/span')
TextoBusqueda = ResultadoBusqueda.text
print("El texto del primer resultado es "+TextoBusqueda)


time.sleep(2)


# Hacer click en el primer resultado
ResultadoBusqueda = driver.find_element(
    By.XPATH, '//h2/a/span')
ResultadoBusqueda.click()
titulo = driver.title
print("El titulo de la pagina es "+titulo)
assert "Selenium" in titulo, "El titulo no tiene la palabra Selenium"


driver.quit()
