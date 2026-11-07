import allure
import pytest
from pages.order_feed_page import OrderFeedPage
from locators.main_page_locators import MainPageLocators
from data import buns_and_ingredients_with_window, ingredients_with_counters

@allure.suite('Проверки главной страницы')
class TestMainPage:
    @allure.title('Проверка перехода на страницу Лента заказов через кнопку навигации с главной страницы')
    def test_order_feed_button_click_from_main_page(self, browser, main_page):
        order_page = OrderFeedPage(browser)
        main_page.click_to_order_feed_button()
        assert order_page.wait_load_order_feed_page()

    @allure.title('Проверка вывода окна описания ингредиета при клике по нему')
    @pytest.mark.parametrize('ingredient, window_ingredient', buns_and_ingredients_with_window)
    def test_click_to_engredients_for_display_info_window(self, main_page, ingredient, window_ingredient):
        main_page.scroll_to_element(ingredient)
        main_page.click_to_element(ingredient)
        assert main_page.wait_load_element(window_ingredient)

    @allure.title('Проверка работоспособности кнопки Крестик в окне описания ингредиента')
    @pytest.mark.parametrize('ingredient, window_ingredient', buns_and_ingredients_with_window)
    def test_click_to_cross_in_engredients_window(self, main_page, ingredient, window_ingredient):
        main_page.scroll_to_element(ingredient)
        main_page.click_to_element(ingredient)
        main_page.wait_load_element(window_ingredient)
        main_page.click_to_cross_button()
        assert main_page.wait_invisibility_element(window_ingredient)

    @allure.title('Проверка изменения значений счетчика булок при добавлении их в конструктор')
    @pytest.mark.parametrize('bun, counter', [(MainPageLocators.BUN_FIRST, MainPageLocators.FIRST_BUN_COUNTER),
                                              (MainPageLocators.BUN_SECOND, MainPageLocators.SECOND_BUN_COUNTER)])
    def test_buns_counter(self, main_page, bun, counter):
        main_page.drag_and_drop_ingredient(bun)
        assert main_page.wait_load_element(counter).text == '2'

    @allure.title('Проверка изменения значений счетчика ингредиента при добавлении его в конструктор')
    @pytest.mark.parametrize('ingredient, counter', ingredients_with_counters)
    def test_ingredients_counter(self, main_page, ingredient, counter):
        main_page.scroll_to_element(ingredient)
        main_page.drag_and_drop_ingredient(ingredient)
        assert main_page.find_element_on_page(counter).text == '1'
