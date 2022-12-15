from selenium.webdriver.common.by import By

from base_page import BasePage


class KeyWebLocators:
    ENTER_BUTTON_LOCATOR = (By.CLASS_NAME, "go_kab")
    CAPTCHA_INPUT_LOCATOR = (By.ID, "captcha")
    ENTER_WITH_PSWD_BUTTON_LOCATOR = (By.ID, "standard_auth_btn")
    BACK_TO_ONE_TIME_CODE_BUTTON_LOCATOR = (By.ID, "back_to_otp_btn")
    PAGE_TITLE_LOCATOR = (By.CSS_SELECTOR, "h1.card-container__title")


class KeyWebPageHelper(BasePage):
    def click_on_enter_button(self):
        return self.find_element(KeyWebLocators.ENTER_BUTTON_LOCATOR).click()

    def click_on_enter_with_pswd_button(self):
        return self.find_element(KeyWebLocators.ENTER_WITH_PSWD_BUTTON_LOCATOR).click()

    def click_on_back_to_one_time_code(self):
        return self.find_element(KeyWebLocators.BACK_TO_ONE_TIME_CODE_BUTTON_LOCATOR).click()

    def input_captcha(self, try_captcha):
        captcha = self.find_element(KeyWebLocators.CAPTCHA_INPUT_LOCATOR)
        captcha.click()
        return captcha.send_keys(try_captcha)

    def check_page_title(self):
        return self.find_element(KeyWebLocators.PAGE_TITLE_LOCATOR).text

