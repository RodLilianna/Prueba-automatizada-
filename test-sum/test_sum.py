import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSum(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.screenshot_dir = os.path.join(os.getcwd(), "test-sum", "screenshot")
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def test_sum_numbers(self):
        self.driver.get("file:///C:/Users/lilianna/OneDrive/Documentos/Prog%203%20(Kelyn%20Tejada)/Tarea-3/Practica%203/Practica%203/VistasHTML/index.html")  # Reemplaza "URL_DE_TU_PAGINA_AQUI" con la URL de tu página

        self.sum_positive_numbers()

        self.sum_negative_numbers()

    def sum_positive_numbers(self):

        self.take_screenshot("before_fields_completed_Pos")

        numero1_input = self.driver.find_element(By.ID, "numero1")
        numero1_input.clear()
        numero1_input.send_keys("5") 

        numero2_input = self.driver.find_element(By.ID, "numero2")
        numero2_input.clear()
        numero2_input.send_keys("3") 

        self.take_screenshot("before_positive_sum")

        sumar_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Sumar')]")
        sumar_button.click()

        time.sleep(2)

        self.take_screenshot("after_positive_sum")

    def sum_negative_numbers(self):

        self.take_screenshot("before_fields_completed_Neg")
        numero1_input = self.driver.find_element(By.ID, "numero1")
        numero1_input.clear()
        numero1_input.send_keys("-9")  

        numero2_input = self.driver.find_element(By.ID, "numero2")
        numero2_input.clear()
        numero2_input.send_keys("-5")  

        self.take_screenshot("before_negative_sum")

        sumar_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Sumar')]")
        sumar_button.click()

        time.sleep(2)

        self.take_screenshot("after_negative_sum")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()