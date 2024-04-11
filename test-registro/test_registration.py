import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge() 

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_dir = os.path.join(os.getcwd(), "test-registro", "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def test_make_successful_user_registration(self):

        self.driver.get("file:///C:/Users/lilianna/OneDrive/Documentos/Prog%203%20(Kelyn%20Tejada)/Tarea-3/Practica%203/Practica%203/VistasHTML/login.html")
        time.sleep(2)

        self.take_screenshot("before_registration")

        username_field = self.driver.find_element(By.NAME, "nombusuario")
        username_field.send_keys("Lilianna123")

        password_field = self.driver.find_element(By.NAME, "contrasena")
        password_field.send_keys("Lilianna123")

        self.take_screenshot("after_fields_completed")

        register_button = self.driver.find_element(By.XPATH, "//button[@onclick='registrarUsuario()']")
        register_button.click()
        time.sleep(5)

        self.take_screenshot("after_registration")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()