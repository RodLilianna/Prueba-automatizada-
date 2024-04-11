import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestLogout(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("file:///C:/Users/lilianna/OneDrive/Documentos/Prog%203%20(Kelyn%20Tejada)/Tarea-3/Practica%203/Practica%203/VistasHTML/index.html")  # Reemplaza "url_de_tu_aplicacion" por la URL real de tu aplicación
        self.screenshot_dir = os.path.join(os.getcwd(), "test-logout", "screenshots")
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def test_logout(self):

        self.take_screenshot("before_logout")

        logout_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='login.html']"))
        )

        self.driver.execute_script("arguments[0].click();", logout_button)

        self.take_screenshot("after_logout")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()