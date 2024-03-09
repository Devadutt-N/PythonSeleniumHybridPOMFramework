from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    txt_email_xpath = "//input[@name='email']"
    txt_password_xpath = "//input[@name='password']"
    btn_login_xpath = "//input[@value='Login']"
    lnk_edit_info_lnk_text = 'Edit your account information'
    lbl_warning_xpath = '//div[@class="alert alert-danger alert-dismissible"]'

    def input_email(self,email_adrs):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email_adrs)

    def input_password(self,pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def validate_edit(self):
        return self.driver.find_element(By.LINK_TEXT, self.lnk_edit_info_lnk_text).is_displayed()

    def validate_warning(self):
        return self.driver.find_element(By.XPATH,self.lbl_warning_xpath).text
