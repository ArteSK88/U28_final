from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'not find {locator}')

    def find_elements(self, locator, time= 30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'not find {locator}')