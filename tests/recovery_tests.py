from pages.auth_page import AuthPageHelper
from pages.recovery_page import RecoveryPageHelper

# python -m pytest -v --driver Chrome --driver-path "./chromedriver" tests/recovery_tests.py


def test_elk_phone_pswd_recovery(browser, elk_open_recovery_page):
    auth_page = AuthPageHelper(browser)
    auth_page.enter_username("1234567890")
    recovery_page = RecoveryPageHelper(browser)
    recovery_page.click_on_continue_button()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"


def test_elk_pnumber_pswd_recovery(browser, elk_open_recovery_page):
    auth_page = AuthPageHelper(browser)
    auth_page.select_pnumber_tab()
    auth_page.enter_username("123456789012")
    recovery_page = RecoveryPageHelper(browser)
    recovery_page.click_on_continue_button()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"
    assert auth_page.check_pnumber_tab_active()


def test_elk_switch_tab_to_email_recovery(browser, elk_open_recovery_page):
    auth_page = AuthPageHelper(browser)
    recovery_page = RecoveryPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("avas@goridze.ru")
    recovery_page.click_on_continue_button()
    assert auth_page.check_mail_tab_active()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"


def test_elk_switch_tab_to_login_recovery(browser, elk_open_recovery_page):
    auth_page = AuthPageHelper(browser)
    recovery_page = RecoveryPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("avas_goridze")
    recovery_page.click_on_continue_button()
    assert auth_page.check_login_tab_active()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"
