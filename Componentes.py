from selenium import webdriver  # Importa el módulo webdriver de Selenium
# Importa el módulo By para localizar elementos
from selenium.webdriver.common.by import By
# Importa el módulo Service para Edge
from selenium.webdriver.edge.service import Service
# Importa el módulo Options para Edge
import time  # Importa el módulo time para agregar retrasos


# Configura el servicio de EdgeDriver
service = Service(r"C:\SeleniumDrivers\msedgedriver.exe")
# Inicializa el controlador de Edge con el servicio y las opciones configuradas
driver = webdriver.Edge(service=service)

driver.get("https://duckduckgo.com/")  # Navega a la página de DuckDuckGo

titulo = driver.title  # Obtiene el título de la página

# Verifica que el título de la página sea "DuckDuckGo - Protección. Privacidad. Tranquilidad."
assert titulo == "DuckDuckGo - Protección. Privacidad. Tranquilidad."

time.sleep(3)  # Agrega un retraso aleatorio

# Encuentra el campo de búsqueda por su nombre
buscar_selenium = driver.find_element(By.NAME, "q")
# Encuentra el botón de búsqueda por su XPath
boton_busqueda = driver.find_element(
    By.XPATH, '//*[@id="searchbox_homepage"]/div/div/div/button')

time.sleep(3)  # Agrega un retraso aleatorio

# Escribe "Selenium" en el campo de búsqueda
buscar_selenium.send_keys("Selenium")
boton_busqueda.click()  # Hace clic en el botón de búsqueda

time.sleep(3)  # Agrega un retraso aleatorio

# Encuentra el campo de búsqueda nuevamente por su nombre
buscar_selenium = driver.find_element(By.NAME, value="q")
# Obtiene el valor del campo de búsqueda
valor = buscar_selenium.get_attribute("value")
# Verifica que el valor del campo de búsqueda sea "Selenium"
assert valor == "Selenium"

driver.quit()  # Cierra el navegador
