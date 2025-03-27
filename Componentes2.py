from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time


service = Service()
driver = webdriver.Edge(service=service)


driver.get("https://duckduckgo.com/")

Buscador = driver.find_element(By.NAME, "q")
Btn = driver.find_element(
    By.XPATH, '//*[@id="searchbox_homepage"]/div/div/div/button')
time.sleep(3)

titulo = driver.title
print("Eltitulo de la pagina es "+titulo)
assert titulo == ("DuckDuckGo - Protección. Privacidad. Tranquilidad.")

Buscador.send_keys("Selenium")
Btn.click()
time.sleep(3)


# verificar que la pagina cargada en efecto buscó la palabra Selenium
Buscador = driver.find_element(By.NAME, "q")
Valor = Buscador.get_attribute("value")
assert Valor == ("Selenium")
time.sleep(3)

print("La palabra buscada fue "+Valor)

driver.quit()
