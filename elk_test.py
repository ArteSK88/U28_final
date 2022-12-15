import pytest

from elk_pages import ElkAuthPageHelper, ElkRegPageHelper, ElkRecoveryPageHelper
from test_data import TestDataSet
import time


# python -m venv venv
# venv\scripts\activate
# python -m pytest -v --driver Chrome --driver-path "./chromedriver" elk_test.py

@pytest.mark.auth
def test_elk_default_tab(browser, elk_open_homepage):
    auth_page = ElkAuthPageHelper(browser)
    assert auth_page.check_tel_tab_active()

@pytest.mark.auth
def test_elk_phone_authorization_with_captcha(browser, elk_open_homepage):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("1234567890")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверно введен текст с картинки"

@pytest.mark.auth
def test_elk_invalid_phone_authorization(browser, elk_open_homepage):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("123456789")
    auth_page.click_on_password()
    assert auth_page.check_phone_format() == "Неверный формат телефона"

@pytest.mark.auth
def test_elk_empty_phone_authorization(browser, elk_open_homepage):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    assert auth_page.check_phone_format() == "Введите номер телефона"

@pytest.mark.auth
def test_elk_email_authorization_with_captcha(browser, elk_open_homepage):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.select_mail_tab()
    auth_page.enter_username("johnnybegood@mail.com")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверно введен текст с картинки"
    assert auth_page.check_mail_tab_active()

@pytest.mark.auth
def test_elk_login_authorization_with_captcha(browser, elk_open_homepage):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.select_login_tab()
    auth_page.enter_username("johnnybegood")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверно введен текст с картинки"
    assert auth_page.check_login_tab_active()

@pytest.mark.auth
def test_elk_pnumber_authorization_with_captcha(browser, elk_open_homepage):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.select_pnumber_tab()
    auth_page.enter_username("123456789101")
    auth_page.enter_password("514168")
    auth_page.click_on_enter_button()
    error_message = auth_page.check_error_message()
    assert error_message == "Неверно введен текст с картинки"
    assert auth_page.check_pnumber_tab_active()


@pytest.mark.reg
@pytest.mark.parametrize("region", [0, 1, 10, 70])
def test_elk_signup_positive(browser, elk_open_sign_up_page, region):
    reg_page = ElkRegPageHelper(browser)
    reg_page.enter_username("Якоб")
    reg_page.enter_surname("Бабкин")
    reg_page.select_region(region)
    email = "yabadabadooooooo@rambler.ru"
    reg_page.enter_email(email)
    reg_page.create_password("123456N8b")
    reg_page.confirm_password("123456N8b")
    reg_page.click_on_register_button()
    assert "Kод подтверждения отправлен на адрес" and email in reg_page.check_confirmation()


@pytest.mark.reg
@pytest.mark.parametrize("firstname", TestDataSet.wrong_name,
                         ids=TestDataSet.wrong_name_ids)
def test_elk_signup_firstname_negative(browser, elk_open_sign_up_page, firstname):
    reg_page = ElkRegPageHelper(browser)
    reg_page.enter_username(firstname)
    reg_page.enter_surname("Бабкин")
    reg_page.select_region(70)
    email = "yabadabadooooooo@rambler.ru"
    reg_page.enter_email(email)
    reg_page.create_password("123456N8b")
    reg_page.confirm_password("123456N8b")
    reg_page.click_on_register_button()
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in reg_page.check_input()


@pytest.mark.reg
@pytest.mark.parametrize("surname", TestDataSet.wrong_name,
                         ids=TestDataSet.wrong_name_ids)
def test_elk_signup_surname_negative(browser, elk_open_sign_up_page, surname):
    reg_page = ElkRegPageHelper(browser)
    reg_page.enter_username("Иван")
    reg_page.enter_surname(surname)
    reg_page.select_region(70)
    email = "yabadabadooooooo@rambler.ru"
    reg_page.enter_email(email)
    reg_page.create_password("123456N8b")
    reg_page.confirm_password("123456N8b")
    reg_page.click_on_register_button()
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in reg_page.check_input()


@pytest.mark.reg
@pytest.mark.parametrize("email", TestDataSet.wrong_phone_or_email,
                         ids=TestDataSet.wrong_phone_or_email_ids)
def test_elk_signup_phone_or_email_negative(browser, elk_open_sign_up_page, email):
    reg_page = ElkRegPageHelper(browser)
    reg_page.enter_username("Иван")
    reg_page.enter_surname("Лапшин")
    reg_page.select_region(70)
    reg_page.enter_email(email)
    reg_page.create_password("123456N8b")
    reg_page.confirm_password("123456N8b")
    reg_page.click_on_register_button()
    assert "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru" \
           in reg_page.check_input()

@pytest.mark.reg
@pytest.mark.parametrize("password", TestDataSet.invalid_pswd,
                         ids=TestDataSet.invalid_pswd_ids)
def test_elk_signup_password_negative(browser, elk_open_sign_up_page, password):
    reg_page = ElkRegPageHelper(browser)
    reg_page.enter_username("Иван")
    reg_page.enter_surname("Лапшин")
    reg_page.select_region(70)
    reg_page.enter_email("johnnybegood@mail.com")
    reg_page.create_password(password)
    reg_page.click_on_confirm_password()
    if password == TestDataSet.invalid_pswd[0]:
        assert reg_page.check_input() == "Длина пароля должна быть не менее 8 символов"
    elif password in [TestDataSet.invalid_pswd[1], TestDataSet.invalid_pswd[3]]:
        assert reg_page.check_input() == "Пароль должен содержать хотя бы одну заглавную букву"
    elif password == TestDataSet.invalid_pswd[2]:
        assert reg_page.check_input() == "Пароль должен содержать хотя бы одну прописную букву"
    elif password == TestDataSet.invalid_pswd[4]:
        assert reg_page.check_input() == "Пароль должен содержать только латинские буквы"
    elif password == TestDataSet.invalid_pswd[5]:
        assert reg_page.check_input() == "Длина пароля должна быть не более 20 символов"
    else:
        assert reg_page.check_input() != ""


@pytest.mark.reg
def test_elk_signup_wo_confirmed_pswd_negative(browser, elk_open_sign_up_page):
    reg_page = ElkRegPageHelper(browser)
    reg_page.enter_username("Иван")
    reg_page.enter_surname("Лапшин")
    reg_page.select_region(70)
    reg_page.enter_email("johnnybegood@mail.com")
    reg_page.create_password("123456N8b")
    reg_page.click_on_register_button()
    assert reg_page.check_input() == "Длина пароля должна быть не менее 8 символов"

@pytest.mark.recovery
def test_elk_phone_pswd_recovery(browser, elk_open_recovery_page):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.enter_username("1234567890")
    recovery_page = ElkRecoveryPageHelper(browser)
    recovery_page.click_on_continue_button()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"


@pytest.mark.recovery
def test_elk_pnumber_pswd_recovery(browser, elk_open_recovery_page):
    auth_page = ElkAuthPageHelper(browser)
    auth_page.select_pnumber_tab()
    auth_page.enter_username("123456789012")
    recovery_page = ElkRecoveryPageHelper(browser)
    recovery_page.click_on_continue_button()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"
    assert auth_page.check_pnumber_tab_active()


@pytest.mark.recovery
def test_elk_switch_tab_to_email_recovery(browser, elk_open_recovery_page):
    auth_page = ElkAuthPageHelper(browser)
    recovery_page = ElkRecoveryPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("avas@goridze.ru")
    recovery_page.click_on_continue_button()
    assert auth_page.check_mail_tab_active()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"


@pytest.mark.recovery
def test_elk_switch_tab_to_login_recovery(browser, elk_open_recovery_page):
    auth_page = ElkAuthPageHelper(browser)
    recovery_page = ElkRecoveryPageHelper(browser)
    auth_page.select_tel_tab()
    auth_page.enter_username("avas_goridze")
    recovery_page.click_on_continue_button()
    assert auth_page.check_login_tab_active()
    assert auth_page.check_error_message() == "Неверный логин или текст с картинки"
