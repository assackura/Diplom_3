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
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']/parent::a")
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    PERSONAL_AREA_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    ORDER_NUMBER_LOCATOR = (By.XPATH, ".//p[contains(@class, 'text_type_digits')]")
    HISTORY_ORDERS_LINK = (By.XPATH, ".//a[contains(text(), 'История заказов')]")
    ORDER_NUMBER = (By.XPATH, "(.//p[contains(@class, 'text_type_digits')])[1]")
    ING_BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    ID_ORDER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")
    CLOSE_BTN_MODAL_WINDOW = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")