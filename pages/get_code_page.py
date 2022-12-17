from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class GetCodeLocators():
    GET_CODE_BUTTON_LOCATOR = (By.ID, "otp_get_code")
    ENTER_WITH_PSWD_BUTTON_LOCATOR = (By.ID, "standard_auth_btn")
    BACK_TO_ONE_TIME_CODE_BUTTON_LOCATOR = (By.ID, "back_to_otp_btn")

    SIX_DIGIT_LOCATOR = (By.CSS_SELECTOR, "div.sdi-container--medium")
    INPUT_CODE_LOCATOR = (By.CSS_SELECTOR, "input.code-input__input")
    CHANGE_EMAIL_LOCATOR = (By.NAME, "otp_back_phone")
    COUNTDOWN_LOCATOR = (By.CSS_SELECTOR, "span.code-input-container__timeout")

    KEYWEB_PAGE_TITLE_LOCATOR = (By.CSS_SELECTOR, "h1.card-container__title")

    SENT_CODE_CONFIRM_TITLE = (By.CSS_SELECTOR, "h1.card-container__title")
    SENT_CODE_CONFIRM_MESSAGE = (By.CSS_SELECTOR, "p.otp-code-form-container__desc")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "p.card-container__error")


class GetCodePageHelper(BasePage):
    def click_on_enter_with_pswd_button(self):
        return self.find_element(GetCodeLocators.ENTER_WITH_PSWD_BUTTON_LOCATOR).click()

    def click_on_back_to_one_time_code(self):
        return self.find_element(GetCodeLocators.BACK_TO_ONE_TIME_CODE_BUTTON_LOCATOR).click()

    def click_on_get_code(self):
        self.find_element(GetCodeLocators.GET_CODE_BUTTON_LOCATOR).click()

    def check_error_message(self):
        return self.find_element(GetCodeLocators.ERROR_MESSAGE_LOCATOR).text

    def keyweb_check_page_title(self):
        return self.find_element(GetCodeLocators.KEYWEB_PAGE_TITLE_LOCATOR).text

    def check_code_input_field(self):
        return self.find_element(GetCodeLocators.SIX_DIGIT_LOCATOR)

    def enter_one_time_code(self, code):
        code_input = self.find_element(GetCodeLocators.INPUT_CODE_LOCATOR)
        return code_input.send_keys(code)

    def check_change_email_link(self):
        return self.find_element(GetCodeLocators.CHANGE_EMAIL_LOCATOR).text

    def check_countdown(self):
        return self.find_element(GetCodeLocators.COUNTDOWN_LOCATOR).text

    def check_sent_code_confirm_title(self):
        return self.find_element(GetCodeLocators.SENT_CODE_CONFIRM_TITLE).text

    def check_sent_code_confirm_message(self):
        return self.find_element(GetCodeLocators.SENT_CODE_CONFIRM_MESSAGE).text