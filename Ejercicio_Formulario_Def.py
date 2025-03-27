from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 📌 **Funciones reutilizables**
def click_elemento(driver, locator, tiempo=3):
    """ Espera a que un elemento sea clickeable y lo hace clic """
    elemento = WebDriverWait(driver, tiempo).until(
        EC.element_to_be_clickable(locator))
    elemento.click()
    return elemento


def ingresar_texto(driver, locator, texto, tiempo=3):
    """ Espera a que un elemento esté presente y le ingresa texto """
    elemento = WebDriverWait(driver, tiempo).until(
        EC.presence_of_element_located(locator))
    elemento.send_keys(texto)
    return elemento


def seleccionar_opcion(driver, locator, opcion, tiempo=3):
    """ Espera a que un elemento sea clickeable y selecciona una opción """
    elemento = WebDriverWait(driver, tiempo).until(
        EC.element_to_be_clickable(locator))
    elemento.send_keys(opcion)
    elemento.send_keys(Keys.RETURN)
    return elemento


def verificar_checkbox(driver, locator, mensaje_error, tiempo=3):
    """ Verifica que un checkbox esté seleccionado """
    elemento = WebDriverWait(driver, tiempo).until(
        EC.presence_of_element_located(locator))
    assert elemento.is_selected(), mensaje_error
    return elemento


def validar_texto(driver, locator, texto_esperado, mensaje_error, tiempo=3):
    """ Verifica que un texto en la web coincida con el esperado """
    elemento = WebDriverWait(driver, tiempo).until(
        EC.presence_of_element_located(locator))
    assert elemento.text == texto_esperado, mensaje_error
    return elemento


def subir_archivo(driver, locator, ruta, tiempo=3):
    """ Sube un archivo a un input de tipo file """
    elemento = WebDriverWait(driver, tiempo).until(
        EC.presence_of_element_located(locator))
    elemento.send_keys(ruta)
    return elemento


# 📌 **Función principal que ejecuta la prueba**
def test_formulario():
    """ Ejecuta la prueba del formulario en DemoQA """
    service = Service()
    driver = webdriver.Edge(service=service)

    try:
        # **Abrir la página**
        driver.get("https://demoqa.com/automation-practice-form")
        driver.maximize_window()

        # **Ingresar datos personales**
        ingresar_texto(driver, (By.ID, 'firstName'), 'Andres')
        ingresar_texto(driver, (By.ID, 'lastName'), 'Quintero')
        ingresar_texto(driver, (By.ID, 'userEmail'), 'andres@gmail.com')
        ingresar_texto(driver, (By.ID, 'userNumber'), '1234567890')

        # **Seleccionar género y hobbies**
        click_elemento(driver, (By.XPATH, "//label[@for='gender-radio-1']"))
        click_elemento(
            driver, (By.XPATH, "//label[@for='hobbies-checkbox-1']"))
        click_elemento(
            driver, (By.XPATH, "//label[@for='hobbies-checkbox-3']"))

        # **Seleccionar fecha de nacimiento**
        click_elemento(driver, (By.ID, 'dateOfBirthInput'))
        seleccionar_opcion(
            driver, (By.CLASS_NAME, "react-datepicker__year-select"), '1988')
        seleccionar_opcion(
            driver, (By.CLASS_NAME, "react-datepicker__month-select"), 'June')
        click_elemento(
            driver, (By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='19']"))

        # **Subir imagen**
        subir_archivo(driver, (By.ID, "uploadPicture"),
                      "C:\\Users\\andres_quintero3\\Desktop\\padmouse.png")

        # **Seleccionar Estado y Ciudad**
        seleccionar_opcion(
            driver, (By.ID, 'react-select-3-input'), 'Uttar Pradesh')
        seleccionar_opcion(driver, (By.ID, 'react-select-4-input'), 'Merrut')

        # **Verificar checkboxes seleccionados**
        verificar_checkbox(driver, (By.ID, 'hobbies-checkbox-1'),
                           "❌ El hobbie Sports no fue seleccionado")
        verificar_checkbox(driver, (By.ID, 'hobbies-checkbox-3'),
                           "❌ El hobbie Music no fue seleccionado")

        # **Enviar formulario**
        click_elemento(driver, (By.ID, 'submit'))

        # **Validaciones en la ventana modal**
        validar_texto(driver, (By.ID, "example-modal-sizes-title-lg"),
                      "Thanks for submitting the form", "❌ No se ingresó a la modal")
        validar_texto(driver, (By.XPATH, "//td[text()='Andres Quintero']"),
                      "Andres Quintero", "❌ El usuario no es correcto")
        validar_texto(driver, (By.XPATH, "//td[text()='andres@gmail.com']"),
                      "andres@gmail.com", "❌ El correo no es correcto")
        validar_texto(
            driver, (By.XPATH, "//td[text()='1234567890']"), "1234567890", "❌ El número no es correcto")

        # **Cerrar el modal**
        click_elemento(driver, (By.ID, 'closeLargeModal'))

        print("✅ Prueba completada exitosamente.")

    except Exception as e:
        print(f"❌ Se produjo un error: {e}")

    finally:
        # **Cerrar navegador**
        driver.quit()


# 📌 **Ejecutar la prueba**
if __name__ == "__main__":
    test_formulario()
