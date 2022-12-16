import pytest
from pages.reg_page import RegPageHelper



@pytest.mark.parametrize("region", [0, 1, 10, 70])
def test_elk_signup_positive(browser, elk_open_sign_up_page, region):
    reg_page = RegPageHelper(browser)
    reg_page.enter_username("Якоб")
    reg_page.enter_surname("Бабкин")
    reg_page.select_region(region)
    email = "yabadabadooooooo@rambler.ru"
    reg_page.enter_email(email)
    reg_page.create_password("123456N8b")
    reg_page.confirm_password("123456N8b")
    reg_page.click_on_register_button()
    assert "Kод подтверждения отправлен на адрес" and email in reg_page.check_confirmation()


