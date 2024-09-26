from selenium.webdriver.common.by import By


class RegisterPageLocators:

    INPUT_NAME_REGISTER = (By.XPATH,
                           ".//form[contains(@class, 'Auth_form')]//label[contains(text(), 'Имя')]/parent::div/input")
    INPUT_EMAIL_REGISTER = (By.XPATH,
                           ".//form[contains(@class, 'Auth_form')]//label[contains(text(), 'Email')]/parent::div/input")
    INPUT_PASSWORD_REGISTER = (By.XPATH,
                           ".//form[contains(@class, 'Auth_form')]//input[contains(@name, 'Пароль')]")
    BUTTON_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Зарегистрироваться']")