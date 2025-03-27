from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

time.sleep(7)
message = driver.find_element(by=By.ID, value="message")
text = message.text

# Verificar si el mensaje es el esperado
if text == "Received!":
    print("El formulario se envió correctamente.")
else:
    print("Hubo un problema al enviar el formulario.")

driver.quit()
