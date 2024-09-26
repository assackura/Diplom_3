from selenium.webdriver.common.by import By


class ResetPageLocators:

    SAVE_BTN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Сохранить']")