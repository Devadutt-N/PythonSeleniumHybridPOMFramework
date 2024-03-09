import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home = HomePage(self.driver)
        home.click_my_account()
        home.select_login()
        login = LoginPage(self.driver)
        login.input_email("testing139@gmail.com")
        login.input_password("welcome@123")
        login.click_login()
        assert login.validate_edit()

    def test_login_with_invalid_credentials(self):
        home = HomePage(self.driver)
        home.click_my_account()
        home.select_login()
        login = LoginPage(self.driver)
        login.input_email("testing123@gmail.com")
        login.input_password("welcome@1234")
        login.click_login()
        expected = "Warning: No match for E-Mail Address and/or Password."
        assert login.validate_warning() == expected
