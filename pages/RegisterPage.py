from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    txt_first_name_id = "input-firstname"
    txt_last_name_id = "input-lastname"
    txt_email_id = "input-email"
    txt_telephone_id = "input-telephone"
    txt_pwd_id = "input-password"
    txt_confirm_id = "input-confirm"
    btn_agree_xpath = "//input[@name='agree']"
    btn_continue_xpath = "//input[@value='Continue']"
    lbl_account_success_xpath = "//div[@id='content']/h1"

    def input_first_name(self, fname):
        self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(fname)

    def input_last_name(self, lname):
        self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(lname)

    def input_email(self, email_id):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email_id)

    def input_telephone(self, phone_num):
        self.driver.find_element(By.ID, self.txt_telephone_id).send_keys(phone_num)

    def input_password(self, pwd):
        self.driver.find_element(By.ID, self.txt_pwd_id).send_keys(pwd)

    def input_confirm_password(self, cpwd):
        self.driver.find_element(By.ID, self.txt_confirm_id).send_keys(cpwd)

    def click_agree(self):
        self.driver.find_element(By.XPATH, self.btn_agree_xpath).click()

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def validate_acc_success(self):
        return self.driver.find_element(By.XPATH, self.lbl_account_success_xpath).text

