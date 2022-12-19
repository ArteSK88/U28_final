import allure
import pytest
from pages.auth_page import AuthPageHelper
from pages.recovery_page import RecoveryPageHelper

from test_data import TestDataSet


@allure.description("обход капчи")
@pytest.mark.parametrize("username", TestDataSet.test_name, ids=TestDataSet.test_name_ids)
@pytest.mark.parametrize("captcha", ["", "N4derN7p"], ids=["empty string", "any value of valid format"])
def test_elk_pswd_recovery_captcha(browser, elk_open_recovery_page, username, captcha):
    auth_page = AuthPageHelper(browser)
    recovery_page = RecoveryPageHelper(browser)
    if username == TestDataSet.test_name[3]:
        auth_page.select_pnumber_tab()
    elif username == username == TestDataSet.test_name[0]:
        auth_page.select_tel_tab()
    else:
        pass
    auth_page.enter_username(username)
    auth_page.input_captcha(captcha)
    recovery_page.click_on_continue_button()
    assert recovery_page.check_captcha()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"
