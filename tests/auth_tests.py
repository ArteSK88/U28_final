from pages.auth_page import AuthPageHelper


# python -m venv venv
# venv\scripts\activate
# python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/auth_tests.py


def test_elk_default_tab(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    assert auth_page.check_tel_tab_active()


def test_elk_phone_authorization_no_such_user(browser, elk_session_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("1234567890")
    auth_page.enter_password("514168")
    if auth_page.check_captcha():
        auth_page.click_on_enter_button()
        assert auth_page.check_error_message() == "Неверно введен текст с картинки"
    else:
        auth_page.click_on_enter_button()
        assert auth_page.check_error_message() == "Неверный логин или пароль"


def test_elk_invalid_phone_authorization(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("123456789")
    auth_page.click_on_password()
    assert auth_page.check_phone_format() == "Неверный формат телефона"


def test_elk_empty_phone_authorization(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    assert auth_page.check_phone_format() == "Введите номер телефона"


def test_elk_email_authorization_with_captcha(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_mail_tab()
    auth_page.enter_username("johnnybegood@mail.com")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверно введен текст с картинки"
    assert auth_page.check_mail_tab_active()


def test_elk_login_authorization_with_captcha(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_login_tab()
    auth_page.enter_username("johnnybegood")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверно введен текст с картинки"
    assert auth_page.check_login_tab_active()


def test_elk_pnumber_authorization_with_captcha(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_pnumber_tab()
    auth_page.enter_username("123456789101")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверно введен текст с картинки"
    assert auth_page.check_pnumber_tab_active()