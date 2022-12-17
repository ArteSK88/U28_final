import pytest
from pages.auth_page import AuthPageHelper
from test_data import TestDataSet

# python -m venv venv
# venv\scripts\activate
# python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/auth_tests.py


def test_elk_default_tab(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    assert auth_page.check_tel_tab_active()


def test_elk_switch_to_email_tab(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("ivanov@mail.ru")
    auth_page.click_on_password()
    assert auth_page.check_email_tab_active()


def test_elk_switch_to_login_tab(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("ivanov")
    auth_page.click_on_password()
    assert auth_page.check_login_tab_active()


def test_elk_switch_to_phone_tab(browser, elk_open_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_email_tab()
    auth_page.enter_username("+79261111111")
    auth_page.click_on_password()
    assert auth_page.check_tel_tab_active()


"""разобраться с куками!!!"""
@pytest.mark.xfail(AuthPageHelper.check_captcha, reason="captcha")
def test_elk_phone_authorization_no_such_user(browser, elk_session_homepage):
    auth_page = AuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("1234567890")
    auth_page.enter_password("514168QaPython")
    auth_page.click_on_enter_button()
    assert auth_page.check_error_message() == "Неверный логин или пароль"


@pytest.mark.xfail(AuthPageHelper.check_captcha, reason="captcha")
@pytest.mark.parametrize("email", TestDataSet.invalid_phone_or_email,
                         ids=TestDataSet.invalid_phone_or_email_ids)
def test_elk_invalid_username_authorization(browser, elk_open_homepage, email):
    auth_page = AuthPageHelper(browser)
    auth_page.enter_username(email)
    auth_page.enter_password("G12345678h")
    auth_page.click_on_enter_button()
    if email == "":
        assert auth_page.check_phone_format() == "Введите номер телефона"
    else:
        assert auth_page.check_error_message() == "Неверный логин или пароль"


@pytest.mark.xfail(AuthPageHelper.check_captcha, reason="captcha")
@pytest.mark.parametrize("password", TestDataSet.invalid_pswd,
                         ids=TestDataSet.invalid_pswd_ids)
def test_elk_invalid_password_authorization(browser, elk_open_homepage, password):
    auth_page = AuthPageHelper(browser)
    auth_page.enter_username('johnnybegood@mail.ru')
    auth_page.enter_password(password)
    auth_page.click_on_enter_button()
    assert auth_page.check_error_message() == "Неверный логин или пароль"