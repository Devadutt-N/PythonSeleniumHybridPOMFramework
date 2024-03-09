from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    txt_search_product_name = "search"
    btn_search_button_xpath = "//span[@class='input-group-btn']/button"
    lnk_my_account_xpath = "//a[@title='My Account']"
    lnk_register_lnk_text = "Register"
    lnk_login_lnk_text = "Login"

    def enter_hp_product(self, prod_name):
        self.driver.find_element(By.NAME, self.txt_search_product_name).send_keys(prod_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.btn_search_button_xpath).click()

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.lnk_my_account_xpath).click()

    def select_register(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_lnk_text).click()

    def select_login(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_lnk_text).click()