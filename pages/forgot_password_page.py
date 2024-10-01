from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage
import allure


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переходим на страницу восстановления пароля')
    def click_recovery_password(self):
        self.click_element(ForgotPasswordLocators.PERSONAL_AREA_LINK, ForgotPasswordLocators.FORGOT_PWD_LINK)
        return self.wait_and_find_element(ForgotPasswordLocators.BUTTON_RESTORE)

    @allure.step('Заполняем поле email на странице восстановления пароля и кликаем по кнопке "Восстановить"')
    def fill_email_and_click_recovery(self, email):
        self.fill_element(ForgotPasswordLocators.INPUT_EMAIL, email)
        self.click_element(ForgotPasswordLocators.BUTTON_RESTORE)
        return self.wait_and_find_element(ForgotPasswordLocators.SAVE_BTN)

    @allure.step('Кликаем по кнопке показать пароль')
    def click_show_hide_password_btn(self):
        self.click_element(ForgotPasswordLocators.DIV_ACTION_SHOW_PASSWORD)
        return self.wait_and_find_element(ForgotPasswordLocators.INPUT_RESET_PASSWORD).get_property("type")
