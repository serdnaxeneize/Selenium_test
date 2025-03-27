from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service()
driver = webdriver.Edge(service=service)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Creando variables
Username = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, 'firstName'))
)
print(f"✅ Se localizó el elemento nombre")


Lastname = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, 'lastName'))
)
print(f"✅ Se localizó el elemento apellido")

Email = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, 'userEmail'))
)
print(f"✅ Se localizó el elemento Email")
Gender = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, "//label[@for='gender-radio-1']"))
)
print(f"✅ Se localizó el elemento genero")


Mobile = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, 'userNumber'))
)
print(f"✅ Se localizó el elemento Mobile")

DoB = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'dateOfBirthInput'))
)
print(f"✅ Se localizó el elemento DoB")

Submit_btn = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'submit'))
)

# Inicio acciones
Username.send_keys('Andres')
Lastname.send_keys('Quintero')
Email.send_keys('andres@gmail.com')
Gender = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, "//label[@for='gender-radio-1']"))
)
Gender.click()

Mobile.send_keys('1234567890')

driver.save_screenshot("Formulario1.png")

DoB.click()
Year_Dob = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "react-datepicker__year-select"))
)
Year_Dob.send_keys('1988')
Year_Dob.send_keys(Keys.RETURN)
print(f"✅ Se ingresó el año de nacimiento")

Month_Dob = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, 'react-datepicker__month-select'))
)
Month_Dob.send_keys('June')
Month_Dob.send_keys(Keys.RETURN)
print(f"✅ Se ingresó el mes de nacimiento")


day_Dob = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='19']"))
)
day_Dob.click()
print(f"✅ Se ingresó el dia de nacimiento")


driver.execute_script("arguments[0].scrollIntoView();", DoB)


Hobbies_sport = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[@for='hobbies-checkbox-1']"))
)
Hobbies_sport.click()
sports_checkbox = driver.find_element(By.ID, 'hobbies-checkbox-1')
assert sports_checkbox.is_selected(), "❌ El hobbie sports no fue seleccionado"
print(f"✅ Se seleccionó Sports")

Hobbies_music = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//label[@for='hobbies-checkbox-3']"))
)
Hobbies_music.click()
Music_checkbox = driver.find_element(By.ID, 'hobbies-checkbox-3')
assert Music_checkbox.is_selected(), "❌ El hobbie Music no fue seleccionado"
print(f"✅ Se seleccionó Music")


driver.save_screenshot("MitadFormulario.png")


Picture = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable(
        (By.ID, "uploadPicture"))
)
Picture.send_keys("C:\\Users\\andres_quintero3\\Desktop\\padmouse.png")
print(f"✅ La imagen se subió correctamente")


Select_state = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'react-select-3-input'))
)
Select_state.send_keys("Uttar Pradesh")
Select_state.send_keys(Keys.RETURN)
print(f"✅ Se seleccionó Estado correctamente")


Select_city = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'react-select-4-input'))
)
Select_city.send_keys("Merrut")
Select_city.send_keys(Keys.RETURN)
print(f"✅ Se seleccionó Ciudad correctamente")


Submit_btn.click()
print(f"✅ Se envió el formulario correctamente")


# validaciones en ventana modal

Text_modal = driver.find_element(By.ID, "example-modal-sizes-title-lg")
Texto_saludo = Text_modal.text
assert "Thanks for submitting the form" in Texto_saludo, "❌ No se ingresó a la modal"
print(f"✅ El texto de la ventana modal es {Texto_saludo}")


Validar_usuario = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, "//td[text()='Andres Quintero']"))
)
Confirmar_usuario = Validar_usuario.text
assert Confirmar_usuario == "Andres Quintero", "❌ El usuario no es correcto"
print(f"✅ EL usuario fue confirmado")

Validar_correo = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, "//td[text()='andres@gmail.com']"))
)
Confirmar_correo = Validar_correo.text
assert Confirmar_correo == "andres@gmail.com", "❌ El correo no es correcto"
print(f"✅ El correo de usuario fue confirmado")

Validar_mobile = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.XPATH, "//td[text()='1234567890']"))
)
Confirmar_mobile = Validar_mobile.text
assert Confirmar_mobile == "1234567890", "❌ El número no es correcto"
print(f"✅ El numero mobile del usuario fue confirmado")
driver.save_screenshot("Ventana_modal.png")

close_modal = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.ID, 'closeLargeModal'))
)
print(f"✅ Se confirma cierre de la ventana modal")

driver.quit()
