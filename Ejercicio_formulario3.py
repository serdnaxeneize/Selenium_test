from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Iniciar el navegador
service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()


# Esperar y ubicar elementos
Name = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "firstName")))
Lastname = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "lastName")))
Email = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "userEmail")))
Number = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "userNumber")))
Gender = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//label[@for="gender-radio-1"]')))
DateInput = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))
Submit = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, "submit")))

print("Los elementos fueron encontrados correctamente.")


# Ingresar datos en los campos
Name.send_keys("Andres")
Lastname.send_keys("Quintero")
Email.send_keys("andresmail@gmail.com")
Gender.click()
Number.send_keys("6987412350")


# Hacer scroll hasta el campo de fecha
driver.execute_script("arguments[0].scrollIntoView();", DateInput)


# Seleccionar calendario
DateInput.click()


# Seleccionar año
Year_dropdown = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))
Year_dropdown.send_keys("1995")
Year_dropdown.send_keys(Keys.ENTER)


# Seleccionar mes
Month_dropdown = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
Month_dropdown.send_keys("August")
Month_dropdown.send_keys(Keys.ENTER)


# Seleccionar día
day = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
    (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']")))
day.click()


# Enviar formulario
Submit.click()


# Verificar confirmación
Texto_ventana = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg")))
assert "Thanks" in Texto_ventana.text, "El mensaje de confirmación no es correcto"


# Verificar número de teléfono
NumeroTelefono = driver.find_element(
    By.XPATH, "//td[text()='6987412350']").text
assert "6987412350" in NumeroTelefono, "El número de teléfono no está presente"
print("El número de teléfono es correcto.")


# Verificar fecha de nacimiento
FechaNacimiento = driver.find_element(
    By.XPATH, "//td[text()='15 August,1995']").text
assert "15 August,1995" in FechaNacimiento, "La fecha de nacimiento no está presente"
print("La fecha de nacimiento es correcta.")


# Verificar correo
Correo = driver.find_element(
    By.XPATH, "//td[text()='andresmail@gmail.com']").text
assert "andresmail@gmail.com" in Correo, "El correo no está presente"
print("El correo es correcto.")


# Tomar captura de pantalla y cerrar modal
driver.save_screenshot("PruebaFormulario3.png")
driver.find_element(By.ID, "closeLargeModal").click()

# Cerrar navegador
driver.quit()
