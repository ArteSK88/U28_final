import pytest

from elk_pages import ElkAuthPageHelper, ElkRegPageHelper, ElkRecoveryPageHelper
from key_web_pages import KeyWebPageHelper
from start_web_pages import StartWebPageHelper
from smarthome_pages import SmarthomePageHelper
from onlime_pages import OnlimePageHelper
from test_data import TestDataSet
import time

@pytest.mark.xfail(reason="captcha")
def test_onlime_get_one_time_code(browser, onlime_open_homepage):
    onlime_homepage = OnlimePageHelper(browser)
    reg_page = ElkRegPageHelper(browser)
    start_web_reg_page = StartWebPageHelper(browser)
    smarthome_page = SmarthomePageHelper(browser)
    email = "mailoedwards@gmail.com"
    reg_page.enter_email(email)
    start_web_reg_page.click_on_get_code()
    assert email in smarthome_page.check_sent_code_confirm_message()
    assert onlime_homepage.check_code_input_field()
    assert onlime_homepage.check_change_email_link()
    assert "Получить код повторно можно через" in onlime_homepage.check_countdown()

