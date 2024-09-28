from selenium.webdriver.common.by import By


class LoginPageLocators:

    FORGOT_PWD_LINK = (By.XPATH, ".//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']")
    INPUT_EMAIL_LOGIN = (By.XPATH,
                         ".//form[contains(@class, 'Auth_form')]//label[contains(text(), 'Email')]/parent::div/input")
    INPUT_PASSWORD_LOGIN = (By.XPATH,
                            ".//form[contains(@class, 'Auth_form')]//input[contains(@name, 'Пароль')]")
    BUTTON_LOGIN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Войти']")