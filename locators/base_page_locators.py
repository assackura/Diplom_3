from selenium.webdriver.common.by import By


class BasePageLocators:

    PERSONAL_AREA_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']/parent::a")
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    ORDER_NUMBER_LOCATOR = (By.XPATH, ".//p[contains(@class, 'text_type_digits')]")



