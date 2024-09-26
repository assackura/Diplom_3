from selenium.webdriver.common.by import By


class ForgotPasswordLocators:

    BUTTON_RESTORE = (
        By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Восстановить']")  # Кнопка "Восстановить"
    INPUT_EMAIL = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//input")
    INPUT_RESET_PASSWORD = (By.XPATH,
                            ".//form[contains(@class, 'Auth_form')]//input[contains(@name, 'Введите новый пароль')]")
    DIV_ACTION_SHOW_PASSWORD = (By.XPATH,
                                ".//form[contains(@class, 'Auth_form')]//div[contains(@class, 'input__icon')]")