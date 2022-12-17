from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class AuthLocators:
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
    KEYWEB_ENTER_BUTTON_LOCATOR = (By.CLASS_NAME, "go_kab")
    FORGOT_PSWD_BUTTON_LOCATOR = (By.ID, "forgot_password")
    FORGOT_PSWD_ACTIVE = (By.CSS_SELECTOR, "a#forgot_password.rt-link--orange")
    ERROR_MESSAGE_LOCATOR = (By.ID, "form-error-message")

    KC_REGISTER_LOCATOR = (By.ID, "kc-register")

    CAPTCHA_LOCATOR = (By.CSS_SELECTOR, "div.login-form__captcha")
    CAPTCHA_INPUT_LOCATOR = (By.ID, "captcha")


class AuthPageHelper(BasePage):

    def select_tel_tab(self):
        tel_tab = self.find_element(AuthLocators.TEL_TAB_LOCATOR)
        return tel_tab.click()

    def check_tel_tab_active(self):
        tel_tab_active = self.find_element(AuthLocators.TEL_TAB_ACTIVE)
        return tel_tab_active

    def select_email_tab(self):
        mail_tab = self.find_element(AuthLocators.MAIL_TAB_LOCATOR)
        return mail_tab.click()

    def check_email_tab_active(self):
        mail_tab_active = self.find_element(AuthLocators.MAIL_TAB_ACTIVE)
        return mail_tab_active

    def select_login_tab(self):
        login_tab = self.find_element(AuthLocators.LOGIN_TAB_LOCATOR)
        return login_tab.click()

    def check_login_tab_active(self):
        login_tab_active = self.find_element(AuthLocators.LOGIN_TAB_ACTIVE)
        return login_tab_active

    def select_pnumber_tab(self):
        pnumber_tab = self.find_element(AuthLocators.PNUMBER_TAB_LOCATOR)
        return pnumber_tab.click()

    def check_pnumber_tab_active(self):
        pnumber_tab_active = self.find_element(AuthLocators.PNUMBER_TAB_ACTIVE)
        return pnumber_tab_active

    def enter_username(self, username):
        username_field = self.find_element(AuthLocators.USERNAME_INPUT_LOCATOR)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def click_on_password(self):
        return self.find_element(AuthLocators.PASSWD_INPUT_LOCATOR).click()

    def enter_password(self, password):
        pswd_field = self.find_element(AuthLocators.PASSWD_INPUT_LOCATOR)
        pswd_field.click()
        pswd_field.send_keys(password)
        return pswd_field

    def click_on_enter_button(self):
        self.find_element(AuthLocators.ENTER_BUTTON_LOCATOR).click()

    def keyweb_click_on_enter_button(self):
        return self.find_element(AuthLocators.KEYWEB_ENTER_BUTTON_LOCATOR).click()

    def click_on_signup_button(self):
        self.find_element(AuthLocators.KC_REGISTER_LOCATOR).click()

    def click_on_forgot_pswd(self):
        self.find_element(AuthLocators.FORGOT_PSWD_BUTTON_LOCATOR).click()

    def check_error_message(self):
        return self.find_element(AuthLocators.ERROR_MESSAGE_LOCATOR).text

    def check_phone_format(self):
        return self.find_element(AuthLocators.PHONE_FORMAT_CHECK).text

    def check_captcha(self):
        return self.find_element(AuthLocators.CAPTCHA_LOCATOR)

    def click_on_captcha(self):
        self.find_element(AuthLocators.CAPTCHA_INPUT_LOCATOR).click()

    def input_captcha(self, try_captcha):
        captcha = self.find_element(AuthLocators.CAPTCHA_INPUT_LOCATOR)
        captcha.click()
        return captcha.send_keys(try_captcha)









