from selenium.webdriver.common.by import By

class BaseLocators:
    BASE_HEADERS_BUTTON_ORDER_FEED = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Лента Заказов']")
    BASE_HEADERS_BUTTON_CONSTRUCTOR = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Конструктор']")
    BASE_HEADERS_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Личный Кабинет']")

    OVERLAY = (By.XPATH, "//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']")

    OVERLAY_ORDER_PLACES = (By.XPATH, "//section[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']")