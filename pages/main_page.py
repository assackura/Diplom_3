from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def constructor_click(self):
        self.wait_and_find_element(BasePageLocators.CONSTRUCTOR_LINK).click()
        return self.wait_and_find_element(BasePageLocators.H1_CONSTRUCTOR_BURGER)

    def order_feed_click(self):
        self.wait_and_find_element(BasePageLocators.ORDER_FEED_LINK).click()
        return self.wait_and_find_element(BasePageLocators.H1_ORDER_FEED)

    def click_ing_bun(self):
        self.wait_and_find_element(MainPageLocators.ING_BUN).click()
        return self.wait_and_find_element(MainPageLocators.H2_BUN_TITLE)

    def click_closed_detail_window_ing(self):
        self.click_ing_bun()
        self.wait_and_find_element(MainPageLocators.CLOSE_BTN_DETAIL_ING).click()
        return self.find_invisible_element(MainPageLocators.H2_BUN_TITLE)

    def add_ing(self):
        self.drag_and_drop_element(MainPageLocators.ING_BUN, MainPageLocators.BASKET_TOP)
        return self.wait_and_find_element(MainPageLocators.COUNTER_BUN)

    def create_new_order(self):
        self.add_ing()
        self.wait_and_find_element(MainPageLocators.BUTTON_CREATE_ORDER).click()
        return self.wait_and_find_element(MainPageLocators.MODAL_ORDER_START)
