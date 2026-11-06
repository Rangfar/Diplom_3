import allure
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.login_page_locators import LoginPageLocators
from constants import Constants

class LoginPage(BasePage):
    @allure.step('Открытие страницы входа в профиль')
    def open_login_page(self):
        self.open_page(Constants.LOGIN_PAGE_URL)
        self.wait_load_login_page()

    @allure.step('Ожидание загрузки страницы входа в профиль')
    def wait_load_login_page(self):
        self.wait_invisibility_element(BaseLocators.OVERLAY)
        self.wait_load_element(LoginPageLocators.LOGIN_PAGE_HEADER)

    @allure.step('Вход в профиль')
    def login_profile(self):
        self.fill_field(LoginPageLocators.EMAIL_INPUT, 'дмитрий_варавва_53_000@mail.ru')
        self.fill_field(LoginPageLocators.PASSWORD_INPUT, '76543210')
        self.click_to_element(LoginPageLocators.INPUT_BUTTON)
