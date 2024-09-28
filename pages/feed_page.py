from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_modal_first_order(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK, FeedPageLocators.FIRST_ORDER_IN_LIST_ORDERS)
        return self.wait_and_find_element(FeedPageLocators.SECTION_MODAL_OPENED)

    def create_new_order(self):
        self.create_order(MainPageLocators.ING_BUN)
        self.click_element(MainPageLocators.CLOSE_BTN_MODAL_WINDOW)

    def get_order_number_from_history_orders(self):
        self.create_order(MainPageLocators.ING_BUN)
        self.click_element(BasePageLocators.PERSONAL_AREA_LINK, AccountPageLocators.HISTORY_ORDERS_LINK)
        return self.wait_and_find_element(AccountPageLocators.ORDER_NUMBER_LOCATOR).text

    def get_list_orders_from_order_feed(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)
        return self.wait_and_find_elements(BasePageLocators.ORDER_NUMBER_LOCATOR)