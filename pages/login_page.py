from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.login_page_locators import LoginPageLocators
from locators.register_page_locators import RegisterPageLocators
from locators.reset_page_locators import ResetPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_area_link(self):
        self.wait_and_find_element(BasePageLocators.PERSONAL_AREA_LINK).click()
        return self.wait_and_find_element(LoginPageLocators.BUTTON_LOGIN)

    def goto_history_orders(self):
        self.wait_and_find_element(BasePageLocators.PERSONAL_AREA_LINK).click()
        self.wait_and_find_element(AccountPageLocators.HISTORY_ORDERS_LINK).click()
        return self.wait_and_find_element(AccountPageLocators.HISTORY_ORDERS_LINK)

    def login_user(self, email, password):
        self.wait_and_find_element(LoginPageLocators.INPUT_PASSWORD_LOGIN).send_keys(password)
        self.wait_and_find_element(LoginPageLocators.INPUT_EMAIL_LOGIN).send_keys(email)
        btn = self.wait_and_find_element(LoginPageLocators.BUTTON_LOGIN)
        self.driver.execute_script("arguments[0].click()", btn)

    def logout_user(self):
        self.click_personal_area_link()
        self.wait_and_find_element(AccountPageLocators.LOGOUT_LINK).click()
        return self.wait_and_find_element(LoginPageLocators.BUTTON_LOGIN)




