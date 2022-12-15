from selenium.webdriver.common.by import By

from base_page import BasePage




class StartWebLocators():
    GET_CODE_BUTTON_LOCATOR = (By.ID, "otp_get_code")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "p.card-container__error")


class StartWebPageHelper(BasePage):
    def click_on_get_code(self):
        self.find_element(StartWebLocators.GET_CODE_BUTTON_LOCATOR).click()

    def check_error_message(self):
        return self.find_element(StartWebLocators.ERROR_MESSAGE_LOCATOR).text




