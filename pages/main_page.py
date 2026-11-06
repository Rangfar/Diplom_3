import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators
from constants import Constants

class MainPage(BasePage):
    @allure.step('Открытие страницы конструктора')
    def open_main_page(self):
        self.open_page(Constants.MAIN_PAGE_URL)
        self.wait_load_main_page()

    @allure.step('Ожидание загрузки страницы конструктора')
    def wait_load_main_page(self):
        self.wait_invisibility_element(BaseLocators.OVERLAY)
        return self.wait_load_element(MainPageLocators.HEADER_MAIN_PAGE)

    @allure.step('Клик по кнопке Крестик в окне информации об ингредиенте')
    def click_to_cross_button(self):
        button = self.wait_load_element(MainPageLocators.CROSS_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Перетаскивание ингредиента в поле конструктора')
    def drag_and_drop_ingredient(self, ingredient):
        drag = self.find_element_on_page(ingredient).find_element(By.XPATH, "..")
        drop = self.find_element_on_page(MainPageLocators.DROP_ZONE)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();
            const dragStart = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragStart);
            const dragEnter = new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dragEnter);
            const dragOver = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dragOver);
            const dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dropEvent);
            const dragEnd = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragEnd);
        """, drag, drop)

    @allure.step('Клик по кнопке Войти в аккаунт')
    def click_to_enter_the_account_button(self):
        self.wait_invisibility_element(BaseLocators.OVERLAY)
        self.click_to_element(MainPageLocators.ENTER_THE_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке Оформить заказ')
    def click_to_place_order_button(self):
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Ожидание загрузки окна Заказ оформлен')
    def wait_load_placed_window(self):
        self.wait_load_element(MainPageLocators.HEADER_PLACED_ORDER_WINDOW)

    @allure.step('Закрытие окна Заказ оформлен')
    def close_placed_order_window(self):
        button = self.wait_load_element(MainPageLocators.CROSS_BUTTON_IN_PLACED_ORDER_WINDOW)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Добавить в конструктор первую в списке булку, соус и начинку')
    def add_bun_sauce_and_filling(self):
        self.drag_and_drop_ingredient(MainPageLocators.BUN_FIRST)
        self.drag_and_drop_ingredient(MainPageLocators.SAUCES_FIRST)
        self.scroll_to_element(MainPageLocators.FILLING_FIRST)
        self.drag_and_drop_ingredient(MainPageLocators.FILLING_FIRST)

    @allure.step('Получение номер заказа с окна Заказ оформлен')
    def get_order_number(self):
        self.wait_text_change(MainPageLocators.ORDER_NUMBER)
        order_number = self.find_element_on_page(MainPageLocators.ORDER_NUMBER)
        return order_number.text

    @allure.step('Ожидание загрузки конструктора')
    def wait_load_drop_zone(self):
        return self.wait_load_element(MainPageLocators.DROP_ZONE)

    def wait_disable_overlay_order_places(self):
        self.wait_invisibility_element(BaseLocators.OVERLAY_ORDER_PLACES)
