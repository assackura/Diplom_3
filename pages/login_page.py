from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем по ссылке "Личный кабинет"(Неавторизованы)')
    def click_personal_area_link(self):
        self.click_element(LoginPageLocators.PERSONAL_AREA_LINK)
        return self.wait_and_find_element(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Кликаем по ссылке "Личный кабинет"(Авторизованы)')
    def click_personal_area_link_auth(self):
        self.click_element(LoginPageLocators.PERSONAL_AREA_LINK)
        return self.wait_and_find_element(LoginPageLocators.LOGOUT_LINK)

    @allure.step('Переходим на страницу с историей заказов')
    def goto_history_orders(self):
        self.click_personal_area_link_auth()
        self.click_element(LoginPageLocators.HISTORY_ORDERS_LINK)
        return self.wait_and_find_element(LoginPageLocators.HISTORY_ORDERS_LINK)

    @allure.step('Выход пользователя')
    def logout_user(self):
        self.click_personal_area_link_auth()
        self.click_element(LoginPageLocators.LOGOUT_LINK)
        return self.wait_and_find_element(LoginPageLocators.BUTTON_LOGIN)




