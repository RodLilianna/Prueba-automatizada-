import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestConversion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()  

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_dir = os.path.join(os.getcwd(), "test-temp", "screenshot")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def test_conversion_fahrenheit_a_celsius(self):

        self.driver.get("file:///C:/Users/lilianna/OneDrive/Documentos/Prog%203%20(Kelyn%20Tejada)/Tarea-3/Practica%203/Practica%203/VistasHTML/index.html")

        self.take_screenshot("before_entering_temperature")

        self.convertir_fahrenheit_a_celsius(12)

    def convertir_fahrenheit_a_celsius(self, temp_fahrenheit):

        temp_fahrenheit_input = self.driver.find_element(By.ID, "TempFahrenheit")
        temp_fahrenheit_input.clear()
        temp_fahrenheit_input.send_keys(str(temp_fahrenheit))

        self.take_screenshot("after_entering_temperature")

        convertir_button = self.driver.find_element(By.XPATH, "//button[@onclick='convertirFahrenheitACelsius()']")
        convertir_button.click()

        time.sleep(2)

        resultado_text = self.driver.find_element(By.ID, "ResultadoFahrenheitACelsius").text
        resultado_esperado = round((temp_fahrenheit - 32) * 5 / 9)

        resultado_text = int(float(resultado_text.split()[0]))

        self.take_screenshot("after_showing_result")

        self.assertEqual(resultado_text, resultado_esperado, "El resultado de la conversión no coincide")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()