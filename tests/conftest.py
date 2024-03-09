import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configurations("basic info", "browser")
    driver = None
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    url = ReadConfigurations.read_configurations("basic info", "url")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()