from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_PAGE_HEADER = (By.XPATH, "//h2[text()='Вход']")

    EMAIL_INPUT = (By.NAME, 'name')
    PASSWORD_INPUT = (By.NAME, 'Пароль')
    INPUT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa'][text()='Войти']")