from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем по ссылке "Конструктор"')
    def constructor_click(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)
        return self.wait_and_find_element(MainPageLocators.H1_CONSTRUCTOR_BURGER)

    @allure.step('Кликаем по ссылке "Лента заказов"')
    def order_feed_click(self):
        self.click_element(MainPageLocators.ORDER_FEED_LINK)
        return self.wait_and_find_element(MainPageLocators.H1_ORDER_FEED)

    @allure.step('Кликаем по ингредиенту')
    def click_ing_bun(self):
        self.click_element(MainPageLocators.ING_BUN)
        return self.wait_and_find_element(MainPageLocators.H2_BUN_TITLE)

    @allure.step('Кликаем по кнопке закрыть модального окна')
    def click_closed_detail_window_ing(self):
        self.click_ing_bun()
        self.click_element(MainPageLocators.CLOSE_BTN_MODAL_WINDOW)
        return self.find_invisible_element(MainPageLocators.H2_BUN_TITLE)

    @allure.step('Увеличиваем счетчик ингредиентов')
    def up_counter_ing(self):
        self.add_ing(MainPageLocators.ING_BUN)
        return self.wait_and_find_element(MainPageLocators.COUNTER_BUN)

    @allure.step('Создаем новый заказ')
    def create_new_order(self):
        self.create_order(MainPageLocators.ING_BUN)
        return self.wait_and_find_element(MainPageLocators.MODAL_ORDER_START)
