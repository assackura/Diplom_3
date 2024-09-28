import allure


class TestMainPage:

    @allure.title('Проверяем переход по клику на кнопку "Конструктор"')
    @allure.description('Тест проверяет переход в конструктор по клику на кнопку "Конструктор"')
    def test_click_constructor(self, main_page):

        assert main_page.constructor_click().is_displayed()

    @allure.title('Проверяем переход по клику на кнопку "Лента заказов"')
    @allure.description('Тест проверяет переход в ленту заказов по клику на кнопку "Лента заказов"')
    def test_click_order_feed(self, main_page):

        assert main_page.order_feed_click().is_displayed()

    @allure.title('Проверяем открытие всплывающего окна "Детали ингредиента"')
    @allure.description('Тест проверяет, что при нажатии на ингредиент, открывает модальное окно с '
                        'деталями по ингредиенту')
    def test_click_ing_open_window_details(self, main_page):

        assert main_page.click_ing_bun().is_displayed()

    @allure.title('Проверяем закрытие модального окна по крестику')
    @allure.description('Тест проверяет, что модальное окно, с подробностями по ингредиенту, закрывает при нажатии на X')
    def test_closed_window_detail_ing_click_x(self, main_page):

        assert not main_page.click_closed_detail_window_ing().is_displayed()

    @allure.title('Проверяем увеличение счетчика ингредиента')
    @allure.description('Тест проверяет, что при переносе ингредиента в корзину увеличивается счетчик ингредиента')
    def test_up_counter_ing_add_ing(self, main_page):

        assert int(main_page.up_counter_ing().text) > 0

    @allure.title('Проверяем создание нового заказа')
    @allure.description('Тест проверяет, что залогиненный пользователь может оформить заказ')
    def test_auth_user_create_new_order(self, main_auth):

        assert main_auth.create_new_order().is_displayed()

