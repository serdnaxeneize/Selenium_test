from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


# Importa WebDriverWait para implementar esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait
# Importa expected_conditions para definir condiciones de espera
from selenium.webdriver.support import expected_conditions as EC
# Importa el módulo Keys para simular la pulsación de teclas
from selenium.webdriver.common.keys import Keys
import time

service = Service()
driver = webdriver.Edge(service=service)

# Navega a la página de carga de archivos
driver.get("https://the-internet.herokuapp.com/upload")


# Espera explícita hasta que el campo de carga de archivos esté presente
file_upload = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "file-upload"))
)
# Envía la ruta del archivo
file_upload.send_keys("C://Users//andres_quintero3//Desktop//padmouse.png")


# Encuentra el botón de envío y lo envía
file_submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "file-submit"))
)
file_submit.submit()  # Hace clic en el botón de envío

# Espera explícita hasta que el mensaje de confirmación esté presente
Confirmation_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h3[text()='File Uploaded!']"))
)

# Verifica si el mensaje de confirmación está presente en la página
if "File Uploaded!" in driver.page_source:
    print("Se subió el archivo correctamente")
else:
    print("El archivo no se subió correctamente")


driver.quit()
