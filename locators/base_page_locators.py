from selenium.webdriver.common.by import By


class BasePageLocators:

    PERSONAL_AREA_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']/parent::a")
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    ORDER_NUMBER_LOCATOR = (By.XPATH, ".//p[contains(@class, 'text_type_digits')]")
    INPUT_PASSWORD_LOGIN = (By.XPATH,
                            ".//form[contains(@class, 'Auth_form')]//input[contains(@name, 'Пароль')]")
    INPUT_EMAIL_LOGIN = (By.XPATH,
                         ".//form[contains(@class, 'Auth_form')]//label[contains(text(), 'Email')]/parent::div/input")
    BUTTON_LOGIN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Войти']")
    BUTTON_CREATE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    BASKET_TOP = (By.XPATH, ".//img[contains(@alt, 'Перетяните булочку сюда (верх)')]/parent::span/parent::div")



