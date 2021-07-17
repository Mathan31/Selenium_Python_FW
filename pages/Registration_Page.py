from selenium.webdriver.support.select import Select


class Registration:
    input_firstname_id = "firstName"
    input_username_id = "email"
    input_email_id = "username"
    drop_title_id = "title"
    text_register_xpath = "//h1[text()='Register']"

    def __init__(self,driver):
        self.driver = driver

    def verify_logo(self):
        result = self.driver.find_element_by_xpath(self.img_UIBank_logo_xpath).is_displayed()
        return result

    def type_first_name(self,username):
        self.driver.find_element_by_id(self.input_firstname_id).clear()
        self.driver.find_element_by_id(self.input_firstname_id).send_keys(username)

    def select_title(self,select):
        search_drop = self.driver.find_element_by_id(self.drop_title_id);
        dropdown = Select(search_drop)
        dropdown.select_by_visible_text(select)



    def verify_register_text(self):
        result = self.driver.find_element_by_xpath(self.text_Welcome_xpath).is_displayed()
        return result

    def click_logout_link(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()