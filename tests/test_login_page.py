import unittest
from time import sleep

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

from tests import constants


class LoginPageTestCase(unittest.TestCase):

    DESIRED_CAPABILITIES = {
        'platformName': constants.PLATFORM_ANDROID,
        'deviceName': 'emulator-5554',
        'appPackage': constants.APP_PACKAGE,
        'appActivity': constants.MAIN_ACTIVITY
    }

    def setUp(self) -> None:
        self.driver = webdriver.Remote(constants.APPIUM_SERVER_URL, LoginPageTestCase.DESIRED_CAPABILITIES)
        self.driver.implicitly_wait(15)
    
    def test_text_of_advance_button(self):
        self._navigate_from_welcome_to_login_page()
        button = self.driver.find_element_by_xpath('//*[@class="android.widget.Button"]')

        self.assertEqual('AVANÇAR >', button.text)

    def test_click_on_advance_without_cpf_raise_popup(self):
        self._navigate_from_welcome_to_login_page()
        edit_text = self.driver.find_element_by_xpath('//*[@class="android.widget.EditText"]')
        button = self.driver.find_element_by_xpath('//*[@class="android.widget.Button"]')

        edit_text.clear()
        button.click()

        self.assertIsNotNone(self.driver.find_element_by_xpath('//*[@text="Oops!!"]'))
    
    def test_click_on_advance_with_cpf_raise_not_popup(self):
        self._navigate_from_welcome_to_login_page()
        edit_text = self.driver.find_element_by_xpath('//*[@class="android.widget.EditText"]')
        button = self.driver.find_element_by_xpath('//*[@class="android.widget.Button"]')

        edit_text.send_keys('04226399072')
        button.click()

        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_xpath('//*[@text="Oops!!"]')

    def tearDown(self) -> None:
        self.driver.quit()

    def _navigate_from_welcome_to_login_page(self):
        button = self.driver.find_element_by_xpath('//*[@resource-id="login-button1"]')
        button.click()
