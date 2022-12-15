import pytest

from elk_pages import ElkAuthPageHelper, ElkRegPageHelper, ElkRecoveryPageHelper
from start_web_pages import StartWebPageHelper
from test_data import TestDataSet


def test_start_web_authorize_captcha(browser, start_web_open_homepage):
    reg_page = ElkRegPageHelper(browser)
    start_web_reg_page = StartWebPageHelper(browser)
    reg_page.enter_email("ivanov@gmail.com")
    start_web_reg_page.click_on_get_code()
    assert start_web_reg_page.check_error_message() == "Неверно введен текст с картинки"


@pytest.mark.parametrize("email", TestDataSet.wrong_phone_or_email,
                         ids=TestDataSet.wrong_phone_or_email_ids)
def test_start_web_authorize_negative(browser, start_web_open_homepage, email):
    reg_page = ElkRegPageHelper(browser)
    start_web_reg_page = StartWebPageHelper(browser)
    reg_page.enter_email(email)
    start_web_reg_page.click_on_get_code()
    assert reg_page.check_input() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, " \
                                     "или email в формате example@email.ru"