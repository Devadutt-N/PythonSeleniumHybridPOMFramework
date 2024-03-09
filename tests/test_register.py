import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_valid_details(self):
        home = HomePage(self.driver)
        home.click_my_account()
        home.select_register()
        register = RegisterPage(self.driver)
        register.input_first_name("Dev1")
        register.input_last_name("D")
        register.input_email("testing" + self.generate_random() + "@gmail.com")
        register.input_telephone("45345345")
        register.input_password("hello@123")
        register.input_confirm_password("hello@123")
        register.click_agree()
        register.click_continue()
        self.expected = "Your Account Has Been Created!"
        assert register.validate_acc_success() == self.expected

    def generate_random(self):
        num = random.random()
        return str(num)
