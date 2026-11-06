from selenium.webdriver.common.by import By

class MainPageLocators:
    HEADER_MAIN_PAGE = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10'][text()='Соберите бургер']")

    ENTER_THE_ACCOUNT_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg'][text()='Оформить заказ']")

    HEADER_PLACED_ORDER_WINDOW = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']/div/p[text()='идентификатор заказа']")
    CROSS_BUTTON_IN_PLACED_ORDER_WINDOW = (By.CSS_SELECTOR, '.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK')

    BUN_FIRST = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Краторная булка N-200i']")
    BUN_SECOND = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Флюоресцентная булка R2-D3']")
    SAUCES_FIRST = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Соус фирменный Space Sauce']")
    SAUCES_SECOND = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Соус традиционный галактический']")
    SAUCES_THIRD = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Соус с шипами Антарианского плоскоходца']")
    SAUCES_FOURTH = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Соус Spicy-X']")
    FILLING_FIRST = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Хрустящие минеральные кольца']")
    FILLING_SECOND = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Плоды Фалленианского дерева']")
    FILLING_THIRD = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Кристаллы марсианских альфа-сахаридов']")
    FILLING_FOURTH = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Мини-салат Экзо-Плантаго']")
    FILLING_FIFTH = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Сыр с астероидной плесенью']")
    FILLING_SIXTH = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Биокотлета из марсианской Магнолии']")
    FILLING_SEVENTH = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Филе Люминесцентного тетраодонтимформа']")
    FILLING_EIGHTH = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Мясо бессмертных моллюсков Protostomia']")
    FILLING_NINTH = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH'][text()='Говяжий метеорит (отбивная)']")

    BUN_FIRST_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Краторная булка N-200i']")
    BUN_SECOND_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Флюоресцентная булка R2-D3']")
    SAUCES_FIRST_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Соус фирменный Space Sauce']")
    SAUCES_SECOND_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Соус традиционный галактический']")
    SAUCES_THIRD_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Соус с шипами Антарианского плоскоходца']")
    SAUCES_FOURTH_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Соус Spicy-X']")
    FILLING_FIRST_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Хрустящие минеральные кольца']")
    FILLING_SECOND_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Плоды Фалленианского дерева']")
    FILLING_THIRD_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Кристаллы марсианских альфа-сахаридов']")
    FILLING_FOURTH_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Мини-салат Экзо-Плантаго']")
    FILLING_FIFTH_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Сыр с астероидной плесенью']")
    FILLING_SIXTH_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Биокотлета из марсианской Магнолии']")
    FILLING_SEVENTH_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Филе Люминесцентного тетраодонтимформа']")
    FILLING_EIGHTH_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Мясо бессмертных моллюсков Protostomia']")
    FILLING_NINTH_WINDOW = (By.XPATH, "//p[@class='text text_type_main-medium mb-8'][text()='Говяжий метеорит (отбивная)']")

    FIRST_BUN_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[1]/a[1]/div/p")
    SECOND_BUN_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[1]/a[2]/div/p")

    FIRST_SAUCES_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[2]/a[1]/div/p")
    SECOND_SAUCES_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[2]/a[2]/div/p")
    THIRD_SAUCES_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[2]/a[3]/div/p")
    FOURTH_SAUCES_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[2]/a[4]/div/p")

    FIRST_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[1]/div/p")
    SECOND_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[2]/div/p")
    THIRD_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[3]/div/p")
    FOURTH_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[4]/div/p")
    FIFTH_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[5]/div/p")
    SIXTH_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[6]/div/p")
    SEVENTH_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[7]/div/p")
    EIGHTH_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[8]/div/p")
    NINTH_FILLING_COUNTER = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[3]/a[9]/div/p")

    CROSS_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div/button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    DROP_ZONE = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]/ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")

    ORDER_NUMBER = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']/div/h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")