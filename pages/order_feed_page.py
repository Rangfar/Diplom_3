import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from constants import Constants

class OrderFeedPage(BasePage):
    @allure.step('Открытие страницы Лента заказов')
    def open_order_feed_page(self):
        self.open_page(Constants.ORDER_FEED_PAGE_URL)
        self.wait_load_order_feed_page()

    @allure.step('Ожидание загрузки страницы Лента заказов')
    def wait_load_order_feed_page(self):
        return self.wait_load_element(OrderFeedLocators.HEADER_ORDER_FEED_PAGE)

    @allure.step('Получение числа выполненных заказов за все время')
    def get_counter_number_of_all_time(self):
        counter = self.find_element_on_page(OrderFeedLocators.COUNTE_OF_ALL_TIME)
        return int(counter.text)

    @allure.step('Получение числа выполненных заказов за сегодня')
    def get_counter_number_of_today(self):
        counter = self.find_element_on_page(OrderFeedLocators.COUNTE_OF_TODAY)
        return int(counter.text)

    @allure.step('Получить верхний номер заказа из списка В работе')
    def get_in_work_section_first_number(self):
        order_number = self.find_element_on_page(OrderFeedLocators.FIRST_NUMBER_IN_WORK_SECTION)
        return order_number.text

    @allure.step('Нормализация номера заказа до 5-ти значного')
    def normalize_the_number(self, order_number):
        while len(order_number) < 5:
            order_number = '0' + order_number
        return order_number