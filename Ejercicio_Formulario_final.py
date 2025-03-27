from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
email = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "userEmail"))
)
gender = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//label[@for="gender-radio-1"]'))
)
phonenumber = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "userNumber"))
)
DoB = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "dateOfBirthInput"))
)

Submit = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, "submit"))
)

print(f"✅ Los elementos fueron encontrados")

# Completar Campos
Name.send_keys("Andres")
Lastname.send_keys("Quintero")
email.send_keys("andresmail@gmail.com")
gender = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//label[@for="gender-radio-1"]'))
)
gender.click()
phonenumber.send_keys("1234567890")

DoB.click()
# Seleccionar año
Year_dropdown = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, 'react-datepicker__year-select'))
)
Year_dropdown.send_keys("1988")
Year_dropdown.send_keys(Keys.RETURN)

# Seleccionar Mes
Month_dropdown = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, 'react-datepicker__month-select'))
)
Month_dropdown.send_keys("June")
Month_dropdown.send_keys(Keys.RETURN)

# Seleccionar dia
Day_dropdown = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='19']"))
)
Day_dropdown.click()

# Hacer scroll
driver.execute_script("arguments[0].scrollIntoView();", Submit)

# Seleccionar hobbies
Sports = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[@for='hobbies-checkbox-1']"))
)
Sports.click()

# validar si esta seleccionado
Sports_checkbox = driver.find_element(By.ID, 'hobbies-checkbox-1')
assert Sports_checkbox.is_selected(), "❌ El hobbie sports no fue seleccionado"

wait = WebDriverWait(driver, 3)
Music = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//label[@for='hobbies-checkbox-3']"))
)

Music.click()

# validar si esta seleccionado
Sports_checkbox = driver.find_element(By.ID, 'hobbies-checkbox-3')
assert Sports_checkbox.is_selected(), "❌ El hobbie music no fue seleccionado"

# Cargar imagen
file_upload = driver.find_element(By.ID, "uploadPicture")
file_upload.send_keys("C:\\Users\\andres_quintero3\\Desktop\\padmouse.png")


# Seleccionar estado
Select_state = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'react-select-3-input'))
)
Select_state.send_keys("Haryana")
Select_state.send_keys(Keys.RETURN)

# Seleccionar ciudad
Select_city = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'react-select-4-input'))
)
Select_city.send_keys("Panipat")
Select_city.send_keys(Keys.RETURN)


# Enviar formulario
Submit.click()


# Ventana emergente
Thanks = driver.find_element(By.ID, "example-modal-sizes-title-lg")
Texto = Thanks.text
assert Texto in "Thanks for submitting the form", "El texto no es el de la ventana emergente"
print(f"✅ El texto de la ventana emergente es correcto")

# validar información
Student_name = driver.find_element(By.XPATH, "//td[text()='Andres Quintero']")
Usuario = Student_name.text
assert Usuario == "Andres Quintero", "El nombre de usuario no es correcto"
print(f"✅ El nombre de usuario es correcto")

student_email = driver.find_element(
    By.XPATH, "//td[text()='andresmail@gmail.com']")

Mail_usuario = student_email.text
assert Mail_usuario == "andresmail@gmail.com", "El correo de usuario no es correcto"
print(f"✅ El correo de usuario es correcto")


# Captura de pantalla
driver.save_screenshot("Ventana_emergente.png")


print(f"✅ Los campos fueron diligenciados")
driver.save_screenshot("Formulario_final.png")

driver.quit()
