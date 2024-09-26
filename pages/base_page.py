import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import GetConfig


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем и ищем нужный нам локатор')
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, GetConfig.get_conf("BrowserParams", "timeout")).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)
