from selenium.webdriver.common.by import By


class MainPageLocators:

    ING_BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    H2_BUN_TITLE = (By.XPATH, ".//h2[contains(text(), 'Детали ингредиента')]")
    CLOSE_BTN_MODAL_WINDOW = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    BASKET_TOP = (By.XPATH, ".//img[contains(@alt, 'Перетяните булочку сюда (верх)')]/parent::span/parent::div")
    COUNTER_BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/parent::a/div[contains(@class, 'counter')]/p")
    MODAL_ORDER_START = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")
    BUTTON_CREATE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    H1_CONSTRUCTOR_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    ID_ORDER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")