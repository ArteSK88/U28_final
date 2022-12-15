from selenium.webdriver.common.by import By

from base_page import BasePage



class OnlimeLocators:
    SIX_DIGIT_LOCATOR = (By.CSS_SELECTOR, "div.sdi-container--medium")
    CHANGE_EMAIL_LOCATOR = (By.NAME, "otp_back_phone")
    COUNTDOWN_LOCATOR = (By.CSS_SELECTOR, "span.code-input-container__timeout")

class OnlimePageHelper(BasePage):
    def check_code_input_field(self):
        return self.find_element(OnlimeLocators.SIX_DIGIT_LOCATOR)

    def check_change_email_link(self):
        return self.find_element(OnlimeLocators.CHANGE_EMAIL_LOCATOR).text

    def check_countdown(self):
        return self.find_element(OnlimeLocators.COUNTDOWN_LOCATOR).text
