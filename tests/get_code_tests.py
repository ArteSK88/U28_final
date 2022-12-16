import pytest
from pages.auth_page import AuthPageHelper
from pages.get_code_page import GetCodePageHelper
from test_data import TestDataSet
from pages.reg_page import RegPageHelper


def test_key_web_one_time_code_captcha(browser, key_web_open_homepage):
    auth_page = AuthPageHelper(browser)
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    auth_page.keyweb_click_on_enter_button()
    reg_page.enter_email("mymail@mail.com")
    auth_page.input_captcha("Aagberef7H")
    get_code_page.click_on_get_code()
    assert auth_page.check_error_message() == "Неверно введен текст с картинки"


def test_key_web_enter_with_pswd_captcha(browser, key_web_open_homepage):
    auth_page = AuthPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    auth_page.keyweb_click_on_enter_button()
    get_code_page.click_on_enter_with_pswd_button()
    auth_page.enter_username("billy")
    auth_page.enter_password("123456N8b")
    auth_page.input_captcha("Aagberef7H")
    auth_page.click_on_enter_button()
    assert auth_page.check_error_message() == "Неверно введен текст с картинки"


def test_key_web_return_to_one_time_code(browser, key_web_open_homepage):
    auth_page = AuthPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    auth_page.keyweb_click_on_enter_button()
    get_code_page.click_on_enter_with_pswd_button()
    get_code_page.click_on_back_to_one_time_code()
    assert get_code_page.keyweb_check_page_title() == "Авторизация по коду"


def test_onlime_get_one_time_code_by_email(browser, onlime_open_homepage):
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    # нужно ввести реальный имейл, для которого есть учетка
    email = "artesk0788@gmail.com"
    # email = "mailoedwards@gmail.com"
    reg_page.enter_email(email)
    get_code_page.click_on_get_code()
    assert email in get_code_page.check_sent_code_confirm_message()
    assert get_code_page.check_code_input_field()
    assert get_code_page.check_change_email_link()
    assert "Получить код повторно можно через" in get_code_page.check_countdown()


def test_smarthome_authorize_captcha(browser, smarthome_open_homepage):
    auth_page = AuthPageHelper(browser)
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    reg_page.enter_email("9266291111")
    get_code_page.click_on_get_code()
    assert auth_page.check_error_message() == "Неверно введен текст с картинки"


@pytest.mark.xfail(reason='captcha')
def test_smarthome_authorize_positive(browser, smarthome_open_homepage):
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    phone = "9266291111"
    reg_page.enter_email(phone)
    get_code_page.click_on_get_code()
    assert get_code_page.check_sent_code_confirm_title() == "Код подтверждения отправлен"
    assert "По SMS на номер " in get_code_page.check_sent_code_confirm_message()


def test_start_web_authorize_captcha(browser, start_web_open_homepage):
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    reg_page.enter_email("ivanov@gmail.com")
    get_code_page.click_on_get_code()
    assert get_code_page.check_error_message() == "Неверно введен текст с картинки"


@pytest.mark.parametrize("email", TestDataSet.wrong_phone_or_email,
                         ids=TestDataSet.wrong_phone_or_email_ids)
def test_start_web_authorize_negative(browser, start_web_open_homepage, email):
    reg_page = RegPageHelper(browser)
    get_code_page = GetCodePageHelper(browser)
    reg_page.enter_email(email)
    get_code_page.click_on_get_code()
    assert reg_page.check_input() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, " \
                                     "или email в формате example@email.ru"