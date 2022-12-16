import pytest
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from pages.auth_page import AuthPageHelper
from test_data import TestUrls


@pytest.fixture(scope='session')
def browser():
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = "85.26.146.169:80"
    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    driver = webdriver.Chrome(executable_path="chromedriver", desired_capabilities=capabilities)
    yield driver
    driver.quit()


@pytest.fixture()
def elk_open_homepage(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    yield

@pytest.fixture()
def elk_session_homepage(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.keep_session(TestUrls.elk)
    yield


@pytest.fixture()
def elk_open_sign_up_page(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.click_on_signup_button()
    yield


@pytest.fixture()
def elk_open_recovery_page(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.elk)
    auth_page.click_on_forgot_pswd()
    yield


@pytest.fixture()
def start_web_open_homepage(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.start_web)
    yield

@pytest.fixture()
def smarthome_open_homepage(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.smarthome)
    yield

@pytest.fixture()
def key_web_open_homepage(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.key_web)
    yield

@pytest.fixture()
def onlime_open_homepage(browser):
    auth_page = AuthPageHelper(browser)
    auth_page.go_to_site(TestUrls.onlime)
    yield

# python -m pytest -v --driver Chrome --driver-path */chromedriver  test.py
