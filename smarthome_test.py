import pytest

from elk_pages import ElkAuthPageHelper, ElkRegPageHelper, ElkRecoveryPageHelper
from start_web_pages import StartWebPageHelper
from smarthome_pages import SmarthomePageHelper
from test_data import TestDataSet


def test_smarthome_authorize_captcha(browser, smarthome_open_homepage):
    reg_page = ElkRegPageHelper(browser)
    start_web_reg_page = StartWebPageHelper(browser)
    reg_page.enter_email("9266291111")
    start_web_reg_page.click_on_get_code()
    assert start_web_reg_page.check_error_message() == "Неверно введен текст с картинки"


@pytest.mark.xfail(reason='captcha')
def test_smarthome_authorize_positive(browser, smarthome_open_homepage):
    reg_page = ElkRegPageHelper(browser)
    start_web_reg_page = StartWebPageHelper(browser)
    smarthome_page = SmarthomePageHelper(browser)
    phone = "9266291111"
    reg_page.enter_email(phone)
    start_web_reg_page.click_on_get_code()
    assert smarthome_page.check_sent_code_confirm_title() == "Код подтверждения отправлен"
    assert "По SMS на номер " in smarthome_page.check_sent_code_confirm_message()
