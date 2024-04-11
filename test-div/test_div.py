import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestConversion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()  
        self.screenshot_dir = os.path.join(os.getcwd(), "test-div", "screenshots")
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def test_conversion_dolares_a_pesos_positivos(self):
        self.driver.get("file:///C:/Users/lilianna/OneDrive/Documentos/Prog%203%20(Kelyn%20Tejada)/Tarea-3/Practica%203/Practica%203/VistasHTML/index.html")

        self.take_screenshot("before_entering_positive_amount")

        self.convertir_dolares_a_pesos(100)

        self.take_screenshot("after_entering_positive_amount")

    def test_conversion_dolares_a_pesos_negativos(self):
        self.driver.get("file:///C:/Users/lilianna/OneDrive/Documentos/Prog%203%20(Kelyn%20Tejada)/Tarea-3/Practica%203/Practica%203/VistasHTML/index.html")

        self.take_screenshot("before_entering_negative_amount")

        self.convertir_dolares_a_pesos(-50)

        self.take_screenshot("after_entering_negative_amount")

    def convertir_dolares_a_pesos(self, cantidad_dolares):
        cantidad_dolares_input = self.driver.find_element(By.ID, "CantidadDolares")
        cantidad_dolares_input.clear()
        cantidad_dolares_input.send_keys(str(cantidad_dolares))

        convertir_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Convertir')]")
        convertir_button.click()

        time.sleep(2)

        self.take_screenshot("after_showing_result")

        resultado_text = self.driver.find_element(By.ID, "ResultadoDolaresAPesos").text
        if cantidad_dolares < 0:
            resultado_esperado = "Cantidad negativa no válida"
        else:
            resultado_calculado = cantidad_dolares * 56.56
            resultado_esperado = "{:.2f}".format(resultado_calculado) if resultado_calculado != int(resultado_calculado) else str(int(resultado_calculado))

        self.assertEqual(resultado_text, resultado_esperado, "El resultado de la conversión no coincide")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()