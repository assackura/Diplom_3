import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import GetConfig


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем и ищем нужный нам локатор')
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, GetConfig.get_conf("BrowserParams", "timeout")).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

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
