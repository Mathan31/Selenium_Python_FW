from pages.Login_Page import Login
from utilities.config_reader import ReadConfig
from utilities.logger import Log
from utilities.excel_reader import Excel

class Test_002_Login:

    URL = ReadConfig.read_config("ApplicationInfo","URL")
    logger = Log.log_generator()
    file_path = r"../data/TC002.xlsx"
    sheet_name = "Sheet1"
    excel = Excel()

    def test_login_multiple(self, browser_init):
        self.logger.info("***********TestCase 3 - Login with multiple valid credential*************")
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
        total_row = self.excel.get_total_row(self.file_path,self.sheet_name)
        for row in range(2,total_row+1):
            user_name = self.excel.get_value(self.file_path,self.sheet_name,row,1)
            password = self.excel.get_value(self.file_path,self.sheet_name,row,2)
            self.login.type_user_name(user_name)
            self.login.type_password(password)
            self.login.click_signin_btn()
            text = self.login.verify_welcome_text()
            if text:
                assert True
                self.logger.info("User reaches to the Home page")
                self.login.click_logout_link()
            else:
                self.driver.save_screenshot(r"../screenshots/" + "test_login_credential_validation.png")
                self.logger.error("User not in the Home page")
                self.driver.quit()
                assert False
        self.driver.quit()




