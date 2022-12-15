from selenium.webdriver.common.by import By

from base_page import BasePage




class SmarthomeLocators():
    SENT_CODE_CONFIRM_TITLE = (By.CSS_SELECTOR, "h1.card-container__title")
    SENT_CODE_CONFIRM_MESSAGE = (By.CSS_SELECTOR, "p.otp-code-form-container__desc")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "p.card-container__error")


class SmarthomePageHelper(BasePage):
    def check_sent_code_confirm_title(self):
        return self.find_element(SmarthomeLocators.SENT_CODE_CONFIRM_TITLE).text

    def check_sent_code_confirm_message(self):
        return self.find_element(SmarthomeLocators.SENT_CODE_CONFIRM_MESSAGE).text
