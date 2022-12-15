import pytest
import time

from elk_pages import ElkAuthPageHelper, ElkRegPageHelper, ElkRecoveryPageHelper
from start_web_pages import StartWebPageHelper
from smarthome_pages import SmarthomePageHelper
from key_web_pages import KeyWebPageHelper
from test_data import TestDataSet


def test_key_web_one_time_code_captcha(browser, key_web_open_homepage):
    key_web_page = KeyWebPageHelper(browser)
    auth_page = ElkAuthPageHelper(browser)
    reg_page = ElkRegPageHelper(browser)
    start_web_reg_page = StartWebPageHelper(browser)
    key_web_page.click_on_enter_button()
    reg_page.enter_email("mymail@mail.com")
    key_web_page.input_captcha("Aagberef7H")
    start_web_reg_page.click_on_get_code()
    assert auth_page.check_error_message() == "Неверно введен текст с картинки"


def test_key_web_enter_with_pswd_captcha(browser, key_web_open_homepage):
    key_web_page = KeyWebPageHelper(browser)
    auth_page = ElkAuthPageHelper(browser)
    key_web_page.click_on_enter_button()
    key_web_page.click_on_enter_with_pswd_button()
    auth_page.enter_username("billy")
    auth_page.enter_password("123456N8b")
    key_web_page.input_captcha("Aagberef7H")
    auth_page.click_on_enter_button()
    assert auth_page.check_error_message() == "Неверно введен текст с картинки"


def test_key_web_return_to_one_time_code(browser, key_web_open_homepage):
    key_web_page = KeyWebPageHelper(browser)
    key_web_page.click_on_enter_button()
    key_web_page.click_on_enter_with_pswd_button()
    key_web_page.click_on_back_to_one_time_code()
    assert key_web_page.check_page_title() == "Авторизация по коду"
