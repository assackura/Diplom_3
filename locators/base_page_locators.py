from selenium.webdriver.common.by import By


class BasePageLocators:

    PERSONAL_AREA_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")  # Ссылка на "личный кабинет"