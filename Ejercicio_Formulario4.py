from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()


Name = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "firstName"))
)
Lastname = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "lastName"))
)
Email = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "userEmail"))
)

Gender = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, "//label[@for='gender-radio-1']"))
)

PhoneNumber = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "userNumber"))
)

DoB = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))
)

Picture = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, "uploadPicture"))
)

Submit = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
print(f"✅ Los elementos fueron localizados")


# Ingresar datos
Name.send_keys("Andres")
Lastname.send_keys("Quintero")
Email.send_keys("andresquintero@mail.com")
Gender.click()
PhoneNumber.send_keys("1234567890")

# Hacer scroll hasta el campo de fecha
driver.execute_script("arguments[0].scrollIntoView();", DoB)


# Seleccionar el calendario
DoB.click()

# Seleccionar el año
Year_dropdown = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "react-datepicker__year-select"))
)
Year_dropdown.send_keys("1988")
Year_dropdown.send_keys(Keys.RETURN)


# Seleccionar el mes
Month_dropdown = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "react-datepicker__month-select"))
)
Month_dropdown.send_keys("June")
Month_dropdown.send_keys(Keys.RETURN)


# Seleccionar el dia
day_dropdown = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class,'react-datepicker__day')and text()='19']"))
)
day_dropdown.click()


# Seleccionar Hobbies

Sports = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[@for='hobbies-checkbox-1']"))
)
Sports.click()


# Verificar que el checkbox esta seleccionado
Sports_checkbox = driver.find_element(By.ID, "hobbies-checkbox-1")
assert Sports_checkbox.is_selected(), "❌ El checkbox de Sports no está seleccionado"
print("✅ El checkbox de Sports está seleccionado correctamente.")


Music = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[@for='hobbies-checkbox-3']"))
)
Music.click()

# Verificar que el checkbox esta seleccionado
Music_checkbox = driver.find_element(By.ID, "hobbies-checkbox-3")
assert Music_checkbox.is_selected(), "❌ El checkbox de Music no está seleccionado"
print("✅ El checkbox de Music está seleccionado correctamente.")


# Buscar y seleccionar la imagen
Picture = driver.find_element(By.ID, 'uploadPicture')
Picture.send_keys("C:\\Users\\andres_quintero3\\Desktop\\padmouse.png")
# Picture.send_keys(r"C:\Users\andres_quintero3\Desktop\padmouse.png")


# Seleccionar estado
Lista_estado = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'react-select-3-input')))
Lista_estado.send_keys("Haryana")  # Escribimos el estado directamente
Lista_estado.send_keys(Keys.RETURN)  # Simulamos Enter para seleccionar

# Seleccionar Ciudad
Lista_ciudad = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, "react-select-4-input"))
)
Lista_ciudad.send_keys("Karnal")  # Escribimos la ciudad directamente
Lista_ciudad.send_keys(Keys.RETURN)  # Simulamos Enter para seleccionar


# Captura de pantalla
driver.save_screenshot("Ejercicio4.png")
# Enviar formulario
Submit.click()

# Verificar en pantalla de confirmación

CloseModal = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'closeLargeModal'))
)

Mensaje_Confirmacion = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg"))
)
NombreUsuario = driver.find_element(
    By.XPATH, ("//td[text()='Andres Quintero']"))
Usuario = NombreUsuario.text
assert Usuario == 'Andres Quintero', '❌ El nombre del usuario no esta en la confirmación'
print(
    f'✅ El nombre del usuario esta en la confirmación, el nombre del usuario es {Usuario}')


CloseModal.click()


driver.quit()
