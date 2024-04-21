import time
import requests
from faker import Faker
import unittest
import pytest
import HtmlTestRunner
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import ChromeDriverManager
from selenium.webdriver.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure_commons.types import AttachmentType

fake = Faker()

class Chrome_CottonByAlena_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_CottonByAlena_1(self):
        driver = self.driver
        driver.get("https://www.cottonbyalena.com/")

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//svg[contains(@preserveAspectRatio,'xMidYMid meet')]")))
        time.sleep(1)  # simulate long-running test

        assert "CottonByAlena - Handmade projects" in driver.title
        print("Page title in Chrome is:", driver.title)



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))