from selenium.webdriver.common.by import By


class FeedPageLocators:

    H1_ORDER_FEED = (By.XPATH, ".//h1[text()='Лента заказов']")
    FIRST_ORDER_IN_LIST_ORDERS = (By.XPATH, "(.//a[contains(@class, 'OrderHistory')])[1]")
    SECTION_MODAL_OPENED = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
    COUNTER_READY_ORDERS_ALL_TIME = (By.XPATH, ".//p[text()='Выполнено за все время:']/"
                                              "parent::div/p[contains(@class, 'OrderFeed')]")
    COUNTER_READY_ORDERS_TODAY = (By.XPATH,
                                 ".//p[text()='Выполнено за сегодня:']/parent::div/p[contains(@class, 'OrderFeed')]")
    ID_ORDER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li")