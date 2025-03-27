from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Espera explícita hasta que el campo de nombre esté presente
Username = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "firstName"))
)

# Espera explícita hasta que el campo de apellido esté presente
Lastname = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "lastName"))
)

# Espera explícita hasta que el campo de correo electrónico esté presente
Email = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "userEmail"))
)

# Espera explícita hasta que el botón de radio de género esté presente
Gender = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "gender-radio-1"))
)

# Espera explícita hasta que el campo de número de teléfono esté presente
UserNumber = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "userNumber"))
)

# Espera explícita hasta que el campo de fecha de nacimiento esté presente
DoB = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'dateOfBirth-label'))
)

# Desplazarse hasta el campo de fecha de nacimiento
driver.execute_script("arguments[0].scrollIntoView();", DoB)

# Espera explícita hasta que el campo de materias esté presente
Subjects = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'subjectsInput'))
)

# Espera explícita hasta que el campo de dirección actual esté presente
CurrentAddress = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'currentAddress'))
)

# Espera explícita hasta que el botón de envío esté presente y sea clicable
submit = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "submit"))
)

# Rellenar el formulario
Username.send_keys("Andres")
Lastname.send_keys("Quintero")
Email.send_keys("andresmail@gmail.com")

# Espera explícita hasta que el botón de radio de género esté presente y sea clicable
Gender = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//label[@for="gender-radio-1"]'))
)
Gender.click()  # Hace clic en el botón de radio de género

UserNumber.send_keys("3174714585")
DoB = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))
)
DoB.click()
# Seleccionar el año
year_dropdown = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "react-datepicker__year-select"))
)
year_dropdown.click()
year_dropdown.send_keys("1988")
year_dropdown.send_keys(Keys.ENTER)

# Seleccionar el mes
month_dropdown = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "react-datepicker__month-select"))
)
month_dropdown.click()
month_dropdown.send_keys("May")
month_dropdown.send_keys(Keys.ENTER)

# Seleccionar el día (por texto visible)
day = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='10']"))
)
day.click()

Subjects.send_keys("Form")
CurrentAddress.send_keys("Andre's address")

# Desplazarse hasta el botón de envío
driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()  # Hace clic en el botón de envío


# Espera explícita hasta que el mensaje de agradecimiento esté presente
Texto = WebDriverWait(driver, 7).until(
    EC.presence_of_element_located((By.ID, 'example-modal-sizes-title-lg'))
)

Palabra = driver.find_element(By.ID, 'example-modal-sizes-title-lg')
Palabra_final = Palabra.text
assert "Thanks" in Palabra_final, "En el texto final no se incluye la palabra Thanks"


# XPath simplificado para encontrar el número de teléfono en la tabla
Numero = driver.find_element(By.XPATH, '//td[text() = "3174714585"]')
Revision_numero = Numero.text
assert "3174714585" in Revision_numero, "El número buscado no es el número digitado"
print(f"El número encontrado es " + Revision_numero)

driver.save_screenshot("prueba_exitosa.png")
print(f"En el texto final si se incluye la palabra " +
      Palabra_final)  # Imprime el mensaje de agradecimiento


Close_button = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, "closeLargeModal"))
)

print(f"La ventana modal se cerró correctamente")
Close_button.click()

time.sleep(5)

driver.quit()
