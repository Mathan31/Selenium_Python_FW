from pages.Login_Page import Login
from pages.Registration_Page import Registration
from utilities.config_reader import ReadConfig
from utilities.logger import Log
import random


class Test_003_Registration:

    URL = ReadConfig.read_config("ApplicationInfo", "URL")
    logger = Log.log_generator()

    def test_registration(self, browser_init):
        print('Get Log Method in TestCase : ', self.logger)
        self.logger.info("**********Test_003_Registration***********")
        self.logger.info("**********Verify Registration ***********")
        self.driver = browser_init
        self.driver.get(self.URL)
        self.lp = Login(self.driver)
        self.lp.click_register_link()
        self.rp = Registration(self.driver)
        result = self.rp.verify_registration_text()
        if result:
            self.logger.info("**********User in Registration Page ***********")
            assert True
        else:
            self.logger.info("**********User Not in Registration Page ***********")
            self.driver.save_screenshot(r"../screenshots/" + "test_not_registration.png")
            assert False

        self.rp.type_first_name("Mathan")
        self.rp.select_title("Mr")
        self.rp.type_middle_name("Pandiyan")
        self.rp.type_last_name("Chandrasekaran")
        self.rp.select_gender("Male")
        name = "Credo"+str(self.gen_random_number())
        self.rp.type_user_name(name)
        email = "credosystemz"+str(self.gen_random_number())+"@gmail.com"
        print('Email',email)
        self.rp.type_email(email)
        self.rp.type_password("testing123")
        self.rp.click_register_button()
        result = self.rp.verify_welcome_text()
        if result:
            self.logger.info("**********User successfully completed the registration ***********")
            assert True
        else:
            self.logger.info("**********User not successfully completed the registration***********")
            self.driver.save_screenshot(r"../screenshots/" + "test_registration_failed.png")
            self.driver.quit()
            assert False
        self.driver.quit()

    def gen_random_number(self):
        return random.randint(1,1000)





