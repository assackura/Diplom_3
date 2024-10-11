from selenium.webdriver.common.by import By


class AccountPageLocators:

    HISTORY_ORDERS_LINK = (By.XPATH, ".//a[contains(text(), 'История заказов')]")
    LOGOUT_LINK = (By.XPATH, ".//button[contains(text(), 'Выход')]")
    ORDER_NUMBER_LOCATOR = (By.XPATH, "(.//p[contains(@class, 'text_type_digits')])[1]")