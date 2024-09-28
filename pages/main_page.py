from locators.base_page_locators import BasePageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def constructor_click(self):
        self.click_element(BasePageLocators.CONSTRUCTOR_LINK)
        return self.wait_and_find_element(MainPageLocators.H1_CONSTRUCTOR_BURGER)

    def order_feed_click(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)
        return self.wait_and_find_element(FeedPageLocators.H1_ORDER_FEED)

    def click_ing_bun(self):
        self.click_element(MainPageLocators.ING_BUN)
        return self.wait_and_find_element(MainPageLocators.H2_BUN_TITLE)

    def click_closed_detail_window_ing(self):
        self.click_ing_bun()
        self.click_element(MainPageLocators.CLOSE_BTN_DETAIL_ING)
        return self.find_invisible_element(MainPageLocators.H2_BUN_TITLE)

    def up_counter_ing(self):
        self.add_ing(MainPageLocators.ING_BUN)
        return self.wait_and_find_element(MainPageLocators.COUNTER_BUN)

    def create_new_order(self):
        self.create_order(MainPageLocators.ING_BUN)
        return self.wait_and_find_element(MainPageLocators.MODAL_ORDER_START)
