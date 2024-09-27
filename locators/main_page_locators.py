from selenium.webdriver.common.by import By


class MainPageLocators:

    ING_BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    H2_BUN_TITLE = (By.XPATH, ".//h2[contains(text(), 'Детали ингредиента')]")
    CLOSE_BTN_DETAIL_ING = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")