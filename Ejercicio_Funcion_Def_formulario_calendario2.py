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


def escribir(driver, locator, texto, time=3):
    elemento = encontrar_elementos(driver, locator, time)
    elemento.send_keys(texto)
    valor_ingresado = elemento.get_attribute("value")
    print(f'Se ingresó {valor_ingresado} en el campo {locator}')
    return valor_ingresado


def imprimir(valor_origen, variable):
    print(f'El texto: {valor_origen} corresponde al texto:{variable}')


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
        driver, (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']"))
    day_dropdown.click()

    print(
        f'La fecha seleccionada fue año {year}, el mes {month}, el dia {day}'
    )


Nombre = escribir(driver, (By.ID, 'firstName'), 'Andres')
Apellido = escribir(driver, (By.ID, 'lastName'), 'Quintero')
Correo = escribir(driver, (By.ID, 'userEmail'), 'andres@gmail.com')
Numero = escribir(driver, (By.ID, 'userNumber'), '1234567890')

imprimir('Andres', Nombre)
imprimir('Quintero', Apellido)
imprimir('Correo', Correo)
imprimir('Número', Numero)


seleccionar_fecha(driver, year=1988, month='june', day=19)


driver.quit()
