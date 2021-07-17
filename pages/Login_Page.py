class Login:
    input_username_id = "username"
    input_password_id = "password"
    button_signin_xpath = "//button[text()='Sign In']"
    link_forgot_xpath = "//small[text()='Forgot Your Password?']"
    link_register_xpath = "//small[text()='Register For Account']"
    img_UIBank_logo_xpath = "//img[@class='vertical-center']"
    text_Welcome_xpath = "//h3[text()=' Welcome! ']"
    link_logout_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def verify_logo(self):
        result = self.driver.find_element_by_xpath(self.img_UIBank_logo_xpath).is_displayed()
        return result

    def type_user_name(self,username):
        self.driver.find_element_by_id(self.input_username_id).clear()
        self.driver.find_element_by_id(self.input_username_id).send_keys(username)

    def type_password(self,password):
        self.driver.find_element_by_id(self.input_password_id).clear()
        self.driver.find_element_by_id(self.input_password_id).send_keys(password)

    def click_signin_btn(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def click_register_link(self):
        self.driver.find_element_by_xpath(self.link_register_xpath).click()

    def verify_welcome_text(self):
        result = self.driver.find_element_by_xpath(self.text_Welcome_xpath).is_displayed()
        return result

    def click_logout_link(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()