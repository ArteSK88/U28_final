import pytest
from pages.auth_page import AuthPageHelper
from pages.get_code_page import GetCodePageHelper
from test_data import TestDataSet
from pages.reg_page import RegPageHelper


@pytest.mark.xfail(AuthPageHelper.check_captcha, reason="captcha")
@pytest.mark.parametrize("email", ["mymail@mail.com", "+79261111111"])
def test_key_web_invalid_one_time_code(browser, key_web_open_homepage, email):
    auth_page = AuthPageHelper(browser)
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    auth_page.keyweb_click_on_enter_button()
    reg_page.enter_email(email)
    get_code_page.click_on_get_code()
    get_code_page.enter_one_time_code("123456")
    assert auth_page.check_error_message() == "Неверный код. Повторите попытку"


def test_key_web_go_to_pswd_auth_page(browser, key_web_open_homepage):
    auth_page = AuthPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    auth_page.keyweb_click_on_enter_button()
    get_code_page.click_on_enter_with_pswd_button()
    assert get_code_page.keyweb_check_page_title() == "Авторизация"


def test_key_web_return_to_one_time_code(browser, key_web_open_homepage):
    auth_page = AuthPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    auth_page.keyweb_click_on_enter_button()
    get_code_page.click_on_enter_with_pswd_button()
    get_code_page.click_on_back_to_one_time_code()
    assert get_code_page.keyweb_check_page_title() == "Авторизация по коду"


@pytest.mark.xfail(AuthPageHelper.check_captcha, reason="captcha and/or email should belong to an existing user")
def test_onlime_get_one_time_code_by_email(browser, onlime_open_homepage):
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    email = "mailoedwards@gmail.com"
    reg_page.enter_email(email)
    get_code_page.click_on_get_code()
    assert email in get_code_page.check_sent_code_confirm_message()
    assert get_code_page.check_code_input_field()
    assert get_code_page.check_change_email_link()
    assert "Получить код повторно можно через" in get_code_page.check_countdown()


@pytest.mark.xfail(AuthPageHelper.check_captcha, reason="captcha")
def test_smarthome_get_code_positive(browser, smarthome_open_homepage):
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    phone = "9266291111"
    reg_page.enter_email(phone)
    get_code_page.click_on_get_code()
    assert get_code_page.check_sent_code_confirm_title() == "Код подтверждения отправлен"
    assert "По SMS на номер " in get_code_page.check_sent_code_confirm_message()


@pytest.mark.parametrize("email", TestDataSet.invalid_phone_or_email,
                         ids=TestDataSet.invalid_phone_or_email_ids)
def test_start_web_invalid_phone_or_email(browser, start_web_open_homepage, email):
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    reg_page.enter_email(email)
    get_code_page.click_on_get_code()
    assert reg_page.check_input() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, " \
                                     "или email в формате example@email.ru"
