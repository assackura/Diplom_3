import allure

from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем модальное окно заказа в ленте')
    def open_modal_first_order(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK, FeedPageLocators.FIRST_ORDER_IN_LIST_ORDERS)
        return self.wait_and_find_element(FeedPageLocators.SECTION_MODAL_OPENED)

    @allure.step('Создаем новый заказ')
    def create_new_order(self):
        self.click_element(BasePageLocators.CONSTRUCTOR_LINK)
        self.create_order(MainPageLocators.ING_BUN)
        number = ""
        while(True):
            number = self.wait_and_find_element(MainPageLocators.ID_ORDER).text
            if number != "9999":
                break
        while(True):
            if len(number) < 7:
                number = "0" + number
            else:
                break
        self.click_element(MainPageLocators.CLOSE_BTN_MODAL_WINDOW)
        return number

    @allure.step('Получаем номер заказа в истории заказов')
    def get_order_number_from_history_orders(self):
        self.create_new_order()
        self.click_element(BasePageLocators.PERSONAL_AREA_LINK, AccountPageLocators.HISTORY_ORDERS_LINK)
        return self.wait_and_find_element(AccountPageLocators.ORDER_NUMBER_LOCATOR).text

    @allure.step('Получаем список заказов в ленте заказов')
    def get_list_orders_from_order_feed(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)
        list_orders = self.wait_and_find_elements(BasePageLocators.ORDER_NUMBER_LOCATOR)
        return_list = []
        for order in list_orders:
            return_list.append(order.text)
        return return_list

    @allure.step('Получаем счетчик заказов за все время')
    def get_counter_ready_orders_all(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)
        return int(self.wait_and_find_element(FeedPageLocators.COUNTER_READY_ORDERS_ALL_TIME).text)

    @allure.step('Получаем счетчик заказов за сегодня')
    def get_counter_ready_orders_today(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)
        return int(self.wait_and_find_element(FeedPageLocators.COUNTER_READY_ORDERS_TODAY).text)

    @allure.step('Получаем номер текущего заказа в работе')
    def get_id_order_in_progress(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)
        number = ""
        while (True):
            number = self.wait_and_find_element(FeedPageLocators.ID_ORDER_IN_PROGRESS).text
            if number != "Все текущие заказы готовы!":
                break
        return number