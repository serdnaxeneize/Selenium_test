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


def encontrar_elementos(driver, locator, time=3):
    return WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))


def escribir_elemento(driver, locator, texto, time=3):
    escribir_elemento = encontrar_elementos(driver, locator, time)
    escribir_elemento.send_keys(texto)
    valor_ingresado = escribir_elemento.get_attribute("value")
    print(f"🤖 Se ingresó {valor_ingresado} en el campo {locator}")
    return valor_ingresado


def seleccionar_fecha(driver, year, month, day, time=3):
    calendario = encontrar_elementos(driver, (By.ID, 'dateOfBirthInput'), time)
    calendario.click()

    year_dropdown = encontrar_elementos(
        driver, (By.CLASS_NAME, 'react-datepicker__year-select'))
    year_dropdown.send_keys(str(year))

    month_dropdown = encontrar_elementos(
        driver, (By.CLASS_NAME, 'react-datepicker__month-select'))
    month_dropdown.send_keys(str(month).capitalize())

    day_dropdown = encontrar_elementos(
        driver, (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{day}']"))
    day_dropdown.click()

    print(f'⏰ La fecha seleccionada fue {day}/{month}/{year}')


def imprimir(textoimpresion, variable):
    print(f'📝 El campo {textoimpresion} fue completado con {variable}')


# Digitar datos
Nombre = escribir_elemento(driver, (By.ID, 'firstName'), 'Andres')
Apellido = escribir_elemento(driver, (By.ID, 'lastName'), 'Quintero')
Correo = escribir_elemento(driver, (By.ID, 'userEmail'), 'andres@gmail.com')
Numero = escribir_elemento(driver, (By.ID, 'userNumber'), '1234567890')

# Imprimir datos ingresados
imprimir('nombre', Nombre)
imprimir('apellido', Apellido)
imprimir('correo', Correo)
imprimir('telefono', Numero)

# Ingresar fecha
seleccionar_fecha(driver, year=1988, month='June', day=19)


driver.quit()
