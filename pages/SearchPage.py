from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    txt_hp_prod_link = "HP LP3065"
    txt_error_prod_msg_xpath = "//input[@value='Search']/following-sibling::p"

    def validate_hp_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.txt_hp_prod_link).is_displayed()

    def validate_error_prod_msg(self):
        return self.driver.find_element(By.XPATH, self.txt_error_prod_msg_xpath).text
