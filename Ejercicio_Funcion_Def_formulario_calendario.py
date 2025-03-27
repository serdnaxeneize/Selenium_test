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

# Función para encontrar elementos en la página con una espera explícita


def encontrar_elementos(driver, locator, time=3):
    return WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))


# Función para ingresar texto en un campo y verificar el valor ingresado
def ingresar_texto(driver, locator, text, time=3):
    elemento = encontrar_elementos(driver, locator, time)
    elemento.send_keys(text)
    valor_ingresado = elemento.get_attribute("value")
    print(f"🤖 Se ingresó {valor_ingresado} en el campo {locator}")
    return valor_ingresado


# Función para imprimir un mensaje con el texto ingresado y el campo correspondiente
def imprimir(textoimpresion, variable):
    print(f"✅ Se ingresó  {textoimpresion} en el campo: {variable}")

# Función para hacer click en el calendario


def seleccionar_fecha(driver, year, month, day, time=3):
    # 1️⃣ Hacer clic en el campo de fecha para abrir el calendario
    calendario = encontrar_elementos(driver, (By.ID, 'dateOfBirthInput'), time)
    calendario.click()

    # 2️⃣ Seleccionar el año en el calendario
    year_dropdown = encontrar_elementos(
        driver, (By.CLASS_NAME, 'react-datepicker__year-select'))
    year_dropdown.send_keys(str(year))

    # 3️⃣ Seleccionar el mes en el calendario
    month_dropdown = encontrar_elementos(
        driver, (By.CLASS_NAME, 'react-datepicker__month-select'))
    month_dropdown.send_keys(str(month).capitalize())

    # 4️⃣ Seleccionar el día en el calendario
    day_element = encontrar_elementos(
        driver, (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"))
    day_element.click()

    # 5️⃣ Mensaje de confirmación
    print(
        f'⏰ La fecha seleccionada fue: {day} de {month} del {year}')


# Llenar el formulario con los datos
Nombre = ingresar_texto(driver, (By.ID, 'firstName'), 'Andres')
Apellido = ingresar_texto(driver, (By.ID, 'lastName'), 'Quintero')
Correo = ingresar_texto(
    driver, (By.ID, 'userEmail'), 'andres@gmail.com')
Telefono = ingresar_texto(driver, (By.ID, 'userNumber'), '1234567890')

# Imprimir los valores ingresados
imprimir('Andres', Nombre)
imprimir('Quintero', Apellido)
imprimir('andres@gmail.com', Correo)
imprimir('1234567890', Telefono)

seleccionar_fecha(driver, year=1988, month="june", day=19)


driver.quit()
