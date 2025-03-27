from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service()
driver = webdriver.Edge(service=service)

driver.get("https://duckduckgo.com/")
time.sleep(2)

titulo = driver.title
print(f"El titulo de la pagina es " + titulo)
assert titulo == ("DuckDuckGo - Protección. Privacidad. Tranquilidad.")


Buscador = driver.find_element(By.NAME, "q")
Btn = driver.find_element(
    By.XPATH, '//*[@id="searchbox_homepage"]/div/div/div/button')
time.sleep(2)


Buscador.send_keys("Python Automation")
Btn.click()
time.sleep(2)

Buscador = driver.find_element(By.NAME, "q")
Valor = Buscador.get_attribute("value")
assert Valor == "Python Automation", "De lo contrario debe dar error"
print(f"El nombre encontrado coincide con el valor buscador y es "+Valor)

driver.quit()
