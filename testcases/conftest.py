from selenium import webdriver
import pytest

@pytest.fixture(params=['chrome','edge'])
def browser_init(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(executable_path=r"../drivers/chromedriver.exe")
    if request.param == 'edge':
        driver = webdriver.Edge(executable_path=r"../drivers/msedgedriver.exe")
    driver.maximize_window()
    driver.set_page_load_timeout(20)
    driver.implicitly_wait(20)
    return driver