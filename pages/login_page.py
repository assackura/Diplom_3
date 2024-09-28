from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_area_link(self):
        self.click_element(BasePageLocators.PERSONAL_AREA_LINK)
        return self.wait_and_find_element(LoginPageLocators.BUTTON_LOGIN)

    def goto_history_orders(self):
        self.click_personal_area_link()
        self.click_element(AccountPageLocators.HISTORY_ORDERS_LINK)
        return self.wait_and_find_element(AccountPageLocators.HISTORY_ORDERS_LINK)

    def logout_user(self):
        self.click_personal_area_link()
        self.click_element(AccountPageLocators.LOGOUT_LINK)
        return self.wait_and_find_element(LoginPageLocators.BUTTON_LOGIN)




