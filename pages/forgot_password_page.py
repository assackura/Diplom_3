from locators.base_page_locators import BasePageLocators
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_recovery_password(self):
        self.wait_and_find_element(BasePageLocators.PERSONAL_AREA_LINK).click()
        self.wait_and_find_element(LoginPageLocators.FORGOT_PWD_LINK).click()

    def fill_email_and_click_recovery(self, email):
        self.wait_and_find_element(ForgotPasswordLocators.INPUT_EMAIL).send_keys(email)
        self.wait_and_find_element(ForgotPasswordLocators.BUTTON_RESTORE).click()

    def click_show_hide_password_btn(self):
        btn = self.wait_and_find_element(ForgotPasswordLocators.DIV_ACTION_SHOW_PASSWORD)
        self.driver.execute_script("arguments[0].click()", btn)
        return self.wait_and_find_element(ForgotPasswordLocators.INPUT_RESET_PASSWORD).get_property("type")
