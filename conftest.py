import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage

@pytest.fixture(params=["chrome", "firefox"], ids=["Chrome", "Firefox"])
def browser(request):
    browser_name = request.param
    allure.dynamic.parameter("Браузер", browser_name)

    if request.param == "chrome":
        browser = webdriver.Chrome()
    elif request.param == "firefox":
        browser = webdriver.Firefox()

    yield browser
    browser.quit()

@pytest.fixture
def prepare_order_feed(browser):
    main_page = MainPage(browser)
    login_page = LoginPage(browser)
    order_feed_page = OrderFeedPage(browser)
    main_page.open_main_page()
    main_page.click_to_enter_the_account_button()
    login_page.wait_load_login_page()
    login_page.login_profile()
    main_page.wait_load_main_page()
    return main_page, order_feed_page

@pytest.fixture
def main_page(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    return main_page

@pytest.fixture
def login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    return login_page

@pytest.fixture
def prepare_per_acc(browser):
    main_page = MainPage(browser)
    login_page = LoginPage(browser)
    personal_account_page = PersonalAccountPage(browser)
    login_page.open_login_page()
    login_page.login_profile()
    return main_page, personal_account_page