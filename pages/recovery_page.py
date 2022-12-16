from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RecoveryLocators:
    CONTINUE_BUTTON_LOCATOR = (By.ID, "reset")
    LOGO_LOCATOR = (By.CSS_SELECTOR, "svg.main-header__logo")


class RecoveryPageHelper(BasePage):
    def click_on_continue_button(self):
        return self.find_element(RecoveryLocators.CONTINUE_BUTTON_LOCATOR).click()

    def click_on_main_logo(self, value):
        return self.find_element(RecoveryLocators.LOGO_LOCATOR).click().send_keys(value)