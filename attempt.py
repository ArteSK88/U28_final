from elk_pages import ElkAuthPageHelper, ElkRegPageHelper, ElkRecoveryPageHelper
from test_data import TestUrls
import time

# python -m venv venv
# venv\scripts\activate
# python -m pytest -v --driver Chrome --driver-path "./chromedriver" elk_test.py


def test_elk_default_tab(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    assert auth_page.check_tel_tab_active()

def test_elk_phone_authorization(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.select_tel_tab()
    auth_page.enter_username("1234567890")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверный логин или пароль" or "Неверно введен текст с картинки"

def test_elk_invalid_phone_authorization(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.select_tel_tab()
    auth_page.enter_username("123456789")
    auth_page.click_on_password()
    assert auth_page.check_phone_format() == "Неверный формат телефона"

def test_elk_empty_phone_authorization(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.select_tel_tab()
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    assert auth_page.check_phone_format() == "Введите номер телефона"

def test_elk_email_authorization(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.select_mail_tab()
    auth_page.enter_username("johnnybegood@mail.com")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверный логин или пароль" or "Неверно введен текст с картинки"
    assert auth_page.check_mail_tab_active()

def test_elk_login_authorization(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.select_login_tab()
    auth_page.enter_username("johnnybegood")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверный логин или пароль" or "Неверно введен текст с картинки"
    assert auth_page.check_login_tab_active()

def test_elk_pnumber_authorization(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.select_pnumber_tab()
    auth_page.enter_username("123456789101")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверный логин или пароль" or "Неверно введен текст с картинки"
    assert auth_page.check_pnumber_tab_active()

def test_elk_signup(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.click_on_signup_button()
    reg_page = ElkRegPageHelper(browser)
    reg_page.enter_username("Яков")
    reg_page.enter_surname("Бабкин")
    reg_page.select_region(70)
    email = "yabadabado@mail.ru"
    reg_page.enter_email(email)
    reg_page.create_password("123456N8b")
    reg_page.confirm_password("123456N8b")
    reg_page.click_on_register_button()
    assert "Kод подтверждения отправлен на адрес" and email in reg_page.check_confirmation()

def test_elk_phone_pswd_recovery(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.click_on_forgot_pswd()
    auth_page.enter_username("1234567890")
    recovery_page = ElkRecoveryPageHelper(browser)
    recovery_page.click_on_continue_button()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"

def test_elk_pnumber_pswd_recovery(browser):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.click_on_forgot_pswd()
    auth_page.select_pnumber_tab()
    auth_page.enter_username("123456789012")
    recovery_page = ElkRecoveryPageHelper(browser)
    recovery_page.click_on_continue_button()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"
    assert auth_page.check_pnumber_tab_active()

def test_elk_switch_tab_to_email_recovery(browser):
    auth_page = ElkAuthPageHelper(browser)
    recovery_page = ElkRecoveryPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.click_on_forgot_pswd()
    auth_page.select_tel_tab()
    auth_page.enter_username("avas@goridze.ru")
    recovery_page.click_on_continue_button()
    assert auth_page.check_mail_tab_active()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"

def test_elk_switch_tab_to_login_recovery(browser):
    auth_page = ElkAuthPageHelper(browser)
    recovery_page = ElkRecoveryPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.click_on_forgot_pswd()
    auth_page.select_tel_tab()
    auth_page.enter_username("avas_goridze")
    recovery_page.click_on_continue_button()
    assert auth_page.check_login_tab_active()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"






# def test_access_abroad(browser):
#     my_page = AuthPageHelper(browser)
#     my_page.go_to_site("https://my.rt.ru/")
#     assert my_page.check_tel_tab_active()