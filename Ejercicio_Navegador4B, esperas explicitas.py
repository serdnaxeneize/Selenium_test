from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el WebDriver
service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://duckduckgo.com/")

# Esperar hasta que el campo de búsqueda esté visible
Buscador = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
BotonBuscador = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="searchbox_homepage"]/div/div/div/button'))
)

# Escribir en la barra de búsqueda y hacer clic en el botón
Buscador.send_keys("Selenium WebDriver")
BotonBuscador.click()

# Esperar a que la página de resultados cargue y validar el título
WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))
titulo = driver.title
print("El título de la página es: " + titulo)
assert "Selenium" in titulo, "El título no tiene la palabra Selenium"

# Esperar hasta que aparezca el primer resultado de búsqueda
ResultadoBusqueda = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//h2/a/span'))
)
TextoBusqueda = ResultadoBusqueda.text
print("El texto del primer resultado es: " + TextoBusqueda)

# Hacer clic en el primer resultado
ResultadoBusqueda.click()

# Esperar a que la nueva página cargue
WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))
titulo = driver.title
print("El título de la nueva página es: " + titulo)
assert "Selenium" in titulo, "El título no tiene la palabra Selenium después de hacer clic"

driver.quit()
