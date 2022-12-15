from selenium.webdriver.common.by import By

from base_page import BasePage



class ElkAuthLocators:
    TEL_TAB_LOCATOR = (By.ID, "t-btn-tab-phone")
    TEL_TAB_ACTIVE = (By.CSS_SELECTOR, "div#t-btn-tab-phone.rt-tab--active")

    MAIL_TAB_LOCATOR = (By.ID, "t-btn-tab-mail")
    MAIL_TAB_ACTIVE = (By.CSS_SELECTOR, "div#t-btn-tab-mail.rt-tab--active")

    LOGIN_TAB_LOCATOR = (By.ID, "t-btn-tab-login")
    LOGIN_TAB_ACTIVE = (By.CSS_SELECTOR, "div#t-btn-tab-login.rt-tab--active")

    PNUMBER_TAB_LOCATOR = (By.ID, "t-btn-tab-ls")
    PNUMBER_TAB_ACTIVE = (By.CSS_SELECTOR, "div#t-btn-tab-ls.rt-tab--active")

    USERNAME_INPUT_LOCATOR = (By.ID, "username")
    PHONE_FORMAT_CHECK = (By.CSS_SELECTOR, "span.rt-input-container__meta--error")
    PASSWD_INPUT_LOCATOR = (By.ID, "password")

    ENTER_BUTTON_LOCATOR = (By.ID, "kc-login")
    FORGOT_PSWD_BUTTON_LOCATOR = (By.ID, "forgot_password")
    FORGOT_PSWD_ACTIVE = (By.CSS_SELECTOR, "a#forgot_password.rt-link--orange")
    ERROR_MESSAGE_LOCATOR = (By.ID, "form-error-message")

    KC_REGISTER_LOCATOR = (By.ID, "kc-register")


class ElkRegisterLocators:
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


class ElkRecoveryLocators:
    CONTINUE_BUTTON_LOCATOR = (By.ID, "reset")
    LOGO_LOCATOR = (By.CSS_SELECTOR, "svg.main-header__logo")


class ElkAuthPageHelper(BasePage):
    def select_tel_tab(self):
        tel_tab = self.find_element(ElkAuthLocators.TEL_TAB_LOCATOR)
        return tel_tab.click()

    def check_tel_tab_active(self):
        tel_tab_active = self.find_element(ElkAuthLocators.TEL_TAB_ACTIVE)
        return tel_tab_active

    def select_mail_tab(self):
        mail_tab = self.find_element(ElkAuthLocators.MAIL_TAB_LOCATOR)
        return mail_tab.click()

    def check_mail_tab_active(self):
        mail_tab_active = self.find_element(ElkAuthLocators.MAIL_TAB_ACTIVE)
        return mail_tab_active

    def select_login_tab(self):
        login_tab = self.find_element(ElkAuthLocators.LOGIN_TAB_LOCATOR)
        return login_tab.click()

    def check_login_tab_active(self):
        login_tab_active = self.find_element(ElkAuthLocators.LOGIN_TAB_ACTIVE)
        return login_tab_active

    def select_pnumber_tab(self):
        pnumber_tab = self.find_element(ElkAuthLocators.PNUMBER_TAB_LOCATOR)
        return pnumber_tab.click()

    def check_pnumber_tab_active(self):
        pnumber_tab_active = self.find_element(ElkAuthLocators.PNUMBER_TAB_ACTIVE)
        return pnumber_tab_active

    def enter_username(self, username):
        username_field = self.find_element(ElkAuthLocators.USERNAME_INPUT_LOCATOR)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def click_on_password(self):
        return self.find_element(ElkAuthLocators.PASSWD_INPUT_LOCATOR).click()

    def enter_password(self, password):
        pswd_field = self.find_element(ElkAuthLocators.PASSWD_INPUT_LOCATOR)
        pswd_field.click()
        pswd_field.send_keys(password)
        return pswd_field

    def click_on_enter_button(self):
        self.find_element(ElkAuthLocators.ENTER_BUTTON_LOCATOR).click()

    def click_on_signup_button(self):
        self.find_element(ElkAuthLocators.KC_REGISTER_LOCATOR).click()

    def click_on_forgot_pswd(self):
        self.find_element(ElkAuthLocators.FORGOT_PSWD_BUTTON_LOCATOR).click()

    def check_error_message(self):
        return self.find_element(ElkAuthLocators.ERROR_MESSAGE_LOCATOR).text

    def check_phone_format(self):
        return self.find_element(ElkAuthLocators.PHONE_FORMAT_CHECK).text


class ElkRegPageHelper(BasePage):
    def enter_username(self, username):
        username_field = self.find_element(ElkRegisterLocators.FIRST_NAME_LOCATOR)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def enter_surname(self, surname):
        surname_field = self.find_element(ElkRegisterLocators.SURNAME_LOCATOR)
        surname_field.click()
        surname_field.send_keys(surname)
        return surname_field

    def select_region(self, region_index):
        self.find_element(ElkRegisterLocators.DROPDOWN_LIST_LOCATOR).click()
        regions = self.find_elements(ElkRegisterLocators.DROPDOWN_VALUES_LOCATOR)
        return regions[region_index].click()

    def enter_email(self, email):
        email_field = self.find_element(ElkRegisterLocators.EMAIL_INPUT_LOCATOR)
        email_field.click()
        email_field.send_keys(email)
        return email_field

    def create_password(self, password):
        pswd_field = self.find_element(ElkRegisterLocators.PASSWD_CREATE_FIELD)
        pswd_field.click()
        pswd_field.send_keys(password)
        return pswd_field

    def click_on_confirm_password(self):
        self.find_element(ElkRegisterLocators.PASSWD_CONFIRM_FIELD).click()

    def confirm_password(self, password2):
        pswd2_field = self.find_element(ElkRegisterLocators.PASSWD_CONFIRM_FIELD)
        pswd2_field.click()
        pswd2_field.send_keys(password2)
        return pswd2_field

    def click_on_register_button(self):
        self.find_element(ElkRegisterLocators.REGISTER_BUTTON_LOCATOR).click()

    def check_confirmation(self):
        return self.find_element(ElkRegisterLocators.CONFIRMATION_MESSAGE_LOCATOR).text

    def check_input(self):
        return self.find_element(ElkRegisterLocators.SIGNUP_WARNING_LOCATOR).text




class ElkRecoveryPageHelper(BasePage):
    def click_on_continue_button(self):
        return self.find_element(ElkRecoveryLocators.CONTINUE_BUTTON_LOCATOR).click()

    def click_on_main_logo(self):
        return self.find_element(ElkRecoveryLocators.LOGO_LOCATOR).click()