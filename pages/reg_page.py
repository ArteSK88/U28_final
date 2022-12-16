from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterLocators:
    FIRST_NAME_LOCATOR = (By.NAME, "firstName")
    SURNAME_LOCATOR = (By.NAME, "lastName")
    EMAIL_INPUT_LOCATOR = (By.ID, "address")
    PASSWD_CREATE_FIELD = (By.ID, "password")
    PASSWD_CONFIRM_FIELD = (By.ID, "password-confirm")
    REGISTER_BUTTON_LOCATOR = (By.NAME, "register")
    CONFIRMATION_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "p.register-confirm-form-container__desc")
    DROPDOWN_LIST_LOCATOR = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    DROPDOWN_VALUES_LOCATOR = (By.CLASS_NAME, "rt-select__list-item")
    SIGNUP_WARNING_LOCATOR = (By.CLASS_NAME, "rt-input-container__meta--error")


class RegPageHelper(BasePage):
    def enter_username(self, username):
        username_field = self.find_element(RegisterLocators.FIRST_NAME_LOCATOR)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def enter_surname(self, surname):
        surname_field = self.find_element(RegisterLocators.SURNAME_LOCATOR)
        surname_field.click()
        surname_field.send_keys(surname)
        return surname_field

    def select_region(self, region_index):
        self.find_element(RegisterLocators.DROPDOWN_LIST_LOCATOR).click()
        regions = self.find_elements(RegisterLocators.DROPDOWN_VALUES_LOCATOR)
        return regions[region_index].click()

    def enter_email(self, email):
        email_field = self.find_element(RegisterLocators.EMAIL_INPUT_LOCATOR)
        email_field.click()
        email_field.send_keys(email)
        return email_field

    def create_password(self, password):
        pswd_field = self.find_element(RegisterLocators.PASSWD_CREATE_FIELD)
        pswd_field.click()
        pswd_field.send_keys(password)
        return pswd_field

    def click_on_confirm_password(self):
        self.find_element(RegisterLocators.PASSWD_CONFIRM_FIELD).click()

    def confirm_password(self, password2):
        pswd2_field = self.find_element(RegisterLocators.PASSWD_CONFIRM_FIELD)
        pswd2_field.click()
        pswd2_field.send_keys(password2)
        return pswd2_field

    def click_on_register_button(self):
        self.find_element(RegisterLocators.REGISTER_BUTTON_LOCATOR).click()

    def check_confirmation(self):
        return self.find_element(RegisterLocators.CONFIRMATION_MESSAGE_LOCATOR).text

    def check_input(self):
        return self.find_element(RegisterLocators.SIGNUP_WARNING_LOCATOR).text