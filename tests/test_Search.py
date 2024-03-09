import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_valid_product(self):
        home = HomePage(self.driver)
        home.enter_hp_product("HP")
        home.click_search_button()
        search = SearchPage(self.driver)
        assert search.validate_hp_product()


    def test_search_for_invalid_product(self):
        home = HomePage(self.driver)
        home.enter_hp_product("Honda")
        home.click_search_button()
        search = SearchPage(self.driver)
        self.expected = 'There is no product that matches the search criteria.'
        assert search.validate_error_prod_msg() == self.expected