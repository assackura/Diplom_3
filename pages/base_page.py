import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import GetConfig
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем и ищем нужный нам локатор')
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, GetConfig.get_conf("BrowserParams", "timeout")).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем и ищем нужные нам локаторы')
    def wait_and_find_elements(self, locator) -> WebElement:
        WebDriverWait(self.driver, GetConfig.get_conf("BrowserParams", "timeout")).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Ожидаем и ищем нужный нам локатор')
    def find_invisible_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, GetConfig.get_conf("BrowserParams", "timeout")).until(
            expected_conditions.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Drag and Drop элемента')
    def drag_and_drop_element(self, locator, target):
        drag = self.wait_and_find_element(locator)
        drop = self.wait_and_find_element(target)
        ac = ActionChains(self.driver)
        ac.drag_and_drop(drag, drop).perform()
        time.sleep(5)

    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Нажимаем на элемент')
    def click_element(self, *locators):
        for locator in locators:
            try:
                self.wait_and_find_element(locator).click()
            except:
                btn = self.wait_and_find_element(locator)
                self.driver.execute_script("arguments[0].click()", btn)

    @allure.step('Заполняем элемент')
    def fill_element(self, locator, value):
        self.wait_and_find_element(locator).send_keys(value)

    @allure.step('Авторизуем пользователя')
    def login_user(self, email, password):
        self.click_element(BasePageLocators.PERSONAL_AREA_LINK)
        self.fill_element(LoginPageLocators.INPUT_PASSWORD_LOGIN, password)
        self.fill_element(LoginPageLocators.INPUT_EMAIL_LOGIN, email)
        self.click_element(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Добавляем ингредиент')
    def add_ing(self, locator):
        self.drag_and_drop_element(locator, MainPageLocators.BASKET_TOP)

    @allure.step('Создаем новый заказ')
    def create_order(self, locator):
        self.add_ing(locator)
        self.click_element(MainPageLocators.BUTTON_CREATE_ORDER)
