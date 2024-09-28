from locators.base_page_locators import BasePageLocators
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.login_page_locators import LoginPageLocators
from locators.reset_page_locators import ResetPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_recovery_password(self):
        self.click_element(BasePageLocators.PERSONAL_AREA_LINK, LoginPageLocators.FORGOT_PWD_LINK)
        return self.wait_and_find_element(ForgotPasswordLocators.BUTTON_RESTORE)

    def fill_email_and_click_recovery(self, email):
        self.fill_element(ForgotPasswordLocators.INPUT_EMAIL, email)
        self.click_element(ForgotPasswordLocators.BUTTON_RESTORE)
        return self.wait_and_find_element(ResetPageLocators.SAVE_BTN)

    def click_show_hide_password_btn(self):
        self.click_element(ForgotPasswordLocators.DIV_ACTION_SHOW_PASSWORD)
        return self.wait_and_find_element(ForgotPasswordLocators.INPUT_RESET_PASSWORD).get_property("type")
