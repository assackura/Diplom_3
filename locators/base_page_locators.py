from selenium.webdriver.common.by import By


class BasePageLocators:

    PERSONAL_AREA_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']/parent::a")
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    H1_CONSTRUCTOR_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    H1_ORDER_FEED = (By.XPATH, ".//h1[text()='Лента заказов']")

