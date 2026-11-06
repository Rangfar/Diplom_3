import allure
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.personal_account_locators import PersonalAccountLocators
from constants import Constants

class PersonalAccountPage(BasePage):
    @allure.step('Открытие станицы Личный кабинет')
    def open_personal_account_page(self):
        self.open_page(Constants.PERSONAL_ACCOUN_URL)
        self.wait_load_personal_account_page()

    @allure.step('Ожидание загрузки страницы Личный кабинет')
    def wait_load_personal_account_page(self):
        self.wait_invisibility_element(BaseLocators.OVERLAY)
        return self.wait_load_element(PersonalAccountLocators.HEADER_PERSONAL_ACCOUNT)
