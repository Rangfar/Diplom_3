import allure

@allure.suite('Проверки страницы Лента заказов')
class TestOrderFeedPage:
    @allure.title('Проверка перехода в Конструктор через кнопки навигации со страницы Лента заказов')
    def test_constructor_button_click_from_order_list(self, prepare_order_feed):
        main_page, order_feed_page = prepare_order_feed
        order_feed_page.open_order_feed_page()
        order_feed_page.click_to_constructor_button()
        assert main_page.wait_load_main_page()

    @allure.title('Проверка изменения значения счетчика выполненых заказа за всё время')
    def test_counter_order_for_all_time(self, prepare_order_feed):
        main_page, order_feed_page = prepare_order_feed
        main_page.click_to_order_feed_button()
        order_feed_page.wait_load_order_feed_page()
        counter = order_feed_page.get_counter_number_of_all_time()
        order_feed_page.click_to_constructor_button()
        main_page.wait_load_drop_zone()
        main_page.add_bun_sauce_and_filling()
        main_page.click_to_place_order_button()
        main_page.wait_load_placed_window()
        main_page.close_placed_order_window()
        main_page.wait_disable_overlay_order_places()
        main_page.click_to_order_feed_button()
        order_feed_page.wait_load_order_feed_page()
        new_counter = order_feed_page.get_counter_number_of_all_time()
        assert new_counter == counter + 1

    @allure.title('Проверка изменения значения счетчика выполненых заказов за сегодня')
    def test_counter_order_for_today(self, prepare_order_feed):
        main_page, order_feed_page = prepare_order_feed
        main_page.click_to_order_feed_button()
        order_feed_page.wait_load_order_feed_page()
        counter = order_feed_page.get_counter_number_of_today()
        order_feed_page.click_to_constructor_button()
        main_page.wait_load_drop_zone()
        main_page.add_bun_sauce_and_filling()
        main_page.click_to_place_order_button()
        main_page.wait_load_placed_window()
        main_page.close_placed_order_window()
        main_page.wait_disable_overlay_order_places()
        main_page.click_to_order_feed_button()
        order_feed_page.wait_load_order_feed_page()
        new_counter = order_feed_page.get_counter_number_of_today()
        assert new_counter == counter + 1

    @allure.title('Проверка добавления номера заказа в секцию В работе')
    def test_in_the_work_section(self, prepare_order_feed):
        main_page, order_feed_page = prepare_order_feed
        main_page.wait_load_drop_zone()
        main_page.add_bun_sauce_and_filling()
        main_page.click_to_place_order_button()
        main_page.wait_load_placed_window()
        order_number = main_page.get_order_number()
        normalize_order_number = order_feed_page.normalize_the_number(order_number)
        main_page.close_placed_order_window()
        main_page.wait_disable_overlay_order_places()
        main_page.click_to_order_feed_button()
        order_feed_page.wait_load_order_feed_page()
        number_in_work = order_feed_page.get_in_work_section_first_number()
        assert normalize_order_number == number_in_work
