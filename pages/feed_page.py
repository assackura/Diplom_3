from locators.base_page_locators import BasePageLocators
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_modal_first_order(self):
        self.wait_and_find_element(BasePageLocators.ORDER_FEED_LINK).click()
        self.wait_and_find_element(FeedPageLocators.FIRST_ORDER_IN_LIST_ORDERS).click()
        return self.wait_and_find_element(FeedPageLocators.CLOSE_BTN_DETAIL_ORDER)