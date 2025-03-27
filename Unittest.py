import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Definición de la clase de prueba que hereda de unittest.TestCase


class usando_unittest(unittest.TestCase):

    # Método que se ejecuta antes de cada prueba
    def setUp(self):
        # Carga el driver usando Service
        service = Service(r"C:\SeleniumDrivers\chromedriver.exe")
        # Pasa el servicio a Chrome()
        self.driver = webdriver.Chrome(service=service)

    # Método de prueba
    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        searchbar = driver.find_element(By.NAME, "q")
        searchbar.send_keys("Selenium")
        searchbar.send_keys(Keys.RETURN)
        time.sleep(5)
        print("Ingreso correcto")
        assert "No se encontró el elemento" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
