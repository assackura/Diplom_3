from selenium.webdriver.common.by import By


class ForgotPasswordLocators:

    BUTTON_RESTORE = (
        By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Восстановить']")  # Кнопка "Восстановить"
    INPUT_EMAIL = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//input")
    INPUT_RESET_PASSWORD = (By.XPATH,
                            ".//form[contains(@class, 'Auth_form')]//input[contains(@name, 'Введите новый пароль')]")
    DIV_ACTION_SHOW_PASSWORD = (By.XPATH,
                                ".//form[contains(@class, 'Auth_form')]//div[contains(@class, 'input__icon')]")
    PERSONAL_AREA_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    FORGOT_PWD_LINK = (By.XPATH, ".//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']")
    SAVE_BTN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Сохранить']")