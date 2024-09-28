from selenium.webdriver.common.by import By


class FeedPageLocators:

    H1_ORDER_FEED = (By.XPATH, ".//h1[text()='Лента заказов']")
    FIRST_ORDER_IN_LIST_ORDERS = (By.XPATH, "(.//a[contains(@class, 'OrderHistory')])[1]")
    SECTION_MODAL_OPENED = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")