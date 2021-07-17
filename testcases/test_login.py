from pages.Login_Page import Login
from utilities.config_reader import ReadConfig
from utilities.logger import Log

class Test_001_Login:

    URL = ReadConfig.read_config("ApplicationInfo","URL")
    user_name = ReadConfig.read_config("ApplicationInfo","username")
    password = ReadConfig.read_config("ApplicationInfo","password")
    logger = Log.log_generator()

    def test_login_title_validation(self,browser_init):
        self.logger.info("***********TestCase 1 - Login Page Validation*************")
        self.driver = browser_init
        self.driver.get(self.URL)
        act_title = self.driver.title
        self.logger.info(f"Title is : {act_title}")
        if act_title == "UiBank":
            assert True
            self.logger.info("User reaches to the login page")
        else:
            self.driver.save_screenshot(r"../screenshots/"+"test_login_title_validation.png")
            self.logger.error("User not in the login page")
            self.driver.quit()
            assert False
        self.driver.quit()

    def test_login(self, browser_init):
        self.logger.info("***********TestCase 2 - Login with valid credential*************")
        self.driver = browser_init
        self.driver.get(self.URL)
        self.login = Login(self.driver)
        result = self.login.verify_logo()
        if result:
            assert True
            self.logger.info("User reaches to the login page")
        else:
            self.driver.save_screenshot(r"../screenshots/" + "test_login_title_validation.png")
            self.logger.error("User not in the login page")
            assert False
        self.login.type_user_name(self.user_name)
        self.login.type_password(self.password)
        self.login.click_signin_btn()
        text = self.login.verify_welcome_text()
        if text:
            assert True
            self.logger.info("User reaches to the Home page")
        else:
            self.driver.save_screenshot(r"../screenshots/" + "test_login_credential_validation.png")
            self.logger.error("User not in the Home page")
            self.driver.quit()
            assert False
        self.login.click_logout_link()
        self.driver.quit()




