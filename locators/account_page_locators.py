from selenium.webdriver.common.by import By


class AccountPageLocators:

    HISTORY_ORDERS_LINK = (By.XPATH, ".//a[contains(text(), 'История заказов')]")
    LOGOUT_LINK = (By.XPATH, ".//button[contains(text(), 'Выход')]")