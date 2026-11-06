import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@allure.suite('Проверки страницы входа в профиль')
class TestLoginPage:
    @allure.title('Проверка перехода на страницу Конструктора через кнопку навигации со страницы входа в профиль')
    def test_constructor_button_click_from_login_page(self, browser, login_page):
            main_page = MainPage(browser)
            login_page.click_to_constructor_button()
            assert main_page.wait_load_main_page()

    @allure.title('Проверка перехода на страницу Лента заказов через кнопку навигации со страницы входа в профиль')
    def test_order_feed_button_click_from_login_page(self, browser, login_page):
            order_feed_page = OrderFeedPage(browser)
            login_page.click_to_order_feed_button()
            assert order_feed_page.wait_load_order_feed_page()