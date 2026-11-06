import allure
from pages.order_feed_page import OrderFeedPage

@allure.suite('Проверки страницы Личный кабинет')
class TestPersonalAccountPage:
    @allure.title('Проверка перехода на страницу Конструктор через кнопки навигации со страницы Личный кабинет')
    def test_constructor_button_click_from_personal_account(self, prepare_per_acc):
        main_page, personal_account_page = prepare_per_acc
        main_page.wait_load_main_page()
        main_page.click_to_personal_account_button()
        personal_account_page.wait_load_personal_account_page()
        personal_account_page.click_to_constructor_button()
        assert main_page.wait_load_main_page()

    @allure.title('Проверка перехода на страницу Лента заказов со страницы Личный кабинет')
    def test_order_feed_button_click_from_personal_account_page(self, browser, prepare_per_acc):
        main_page, personal_account_page = prepare_per_acc
        order_feed_page = OrderFeedPage(browser)
        main_page.wait_load_main_page()
        main_page.click_to_personal_account_button()
        personal_account_page.wait_load_personal_account_page()
        personal_account_page.click_to_order_feed_button()
        assert order_feed_page.wait_load_order_feed_page()