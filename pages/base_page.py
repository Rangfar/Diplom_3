import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_locators import BaseLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def wait_load_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def fill_field(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    def find_element_on_page(self, locator):
        return self.driver.find_element(*locator)

    def wait_text_change(self, locator):
        return WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element(*locator).text != '9999')

    def wait_clickable_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Клик по кнопке Конструктор в навигации страницы')
    def click_to_constructor_button(self):
        self.click_to_element(BaseLocators.BASE_HEADERS_BUTTON_CONSTRUCTOR)

    @allure.step('Клик по кнопке Лента заказов в навигации страницы')
    def click_to_order_feed_button(self):
        self.click_to_element(BaseLocators.BASE_HEADERS_BUTTON_ORDER_FEED)

    @allure.title('Клик по кнопке Личный кабинет в навигации страницы')
    def click_to_personal_account_button(self):
        self.click_to_element(BaseLocators.BASE_HEADERS_BUTTON_PERSONAL_ACCOUNT)