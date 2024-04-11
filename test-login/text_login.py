import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.screenshot_dir = os.path.join(os.getcwd(), "test-login", "screenshot")
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def test_make_login_succeed(self):
        self.driver.get("file:///C:/Users/lilianna/OneDrive/Documentos/Prog%203%20(Kelyn%20Tejada)/Tarea-3/Practica%203/Practica%203/VistasHTML/login.html")
        time.sleep(2)
        self.take_screenshot("before_login_valid_credentials")

        username_field = self.driver.find_element(By.NAME, "nombusuario")
        username_field.send_keys("lili")

        password_field = self.driver.find_element(By.NAME, "contrasena")
        password_field.send_keys("123")

        self.take_screenshot("after_valid_credentials_completed")

        login_button = self.driver.find_element(By.XPATH, "//button[@onclick='iniciarSesion()']")
        login_button.click()
        time.sleep(5)

        self.take_screenshot("after_login_valid_credentials")


    def test_make_login_fail(self):
        self.driver.get("file:///C:/Users/lilianna/OneDrive/Documentos/Prog%203%20(Kelyn%20Tejada)/Tarea-3/Practica%203/Practica%203/VistasHTML/login.html")
        time.sleep(2)

        self.take_screenshot("before_login_invalid_credentials")

        username_field = self.driver.find_element(By.NAME, "nombusuario")
        username_field.send_keys("Lilianna123")

        password_field = self.driver.find_element(By.NAME, "contrasena")
        password_field.send_keys("lilianna123")

        self.take_screenshot("after_invalid_credentials_completed")

        login_button = self.driver.find_element(By.XPATH, "//button[@onclick='iniciarSesion()']")
        login_button.click()
        time.sleep(5)
        
        self.take_screenshot("after_login_invalid_credentials")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()