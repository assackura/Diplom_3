import allure


class TestFeedPage:

    @allure.title('Проверяем открытие всплывающего окна с деталями заказа')
    @allure.description('Тест проверяет открытие модального окна, с деталями заказа, на странице лента заказов,'
                        ' по клику на заказ')
    def test_click_order_open_details(self, feed_page):

        assert feed_page.open_modal_first_order().is_displayed()

    @allure.title('Проверяем заказ из истории заказов в ленте заказов')
    @allure.description('Тест проверяет наличие заказа из истории заказов в ленте заказов')
    def test_displayed_order_history_in_order_feed(self, feed_auth):
        histrory_order = feed_auth.get_order_number_from_history_orders()
        list_orders_feed = feed_auth.get_list_orders_from_order_feed()

        assert histrory_order in list_orders_feed

    @allure.title('Проверяем увеличение счетчика "Выполнено за все время"')
    @allure.description('Тест проверяет увеличение счетчика заказов на странице "Лента заказов" за все время')
    def test_up_counter_all_time_after_order(self, feed_auth):
        before = feed_auth.get_counter_ready_orders_all()
        feed_auth.create_new_order()
        after = feed_auth.get_counter_ready_orders_all()

        assert after > before

    @allure.title('Проверяем увеличение счетчика "Выполнено за сегодня"')
    @allure.description('Тест проверяет увеличение счетчика заказов на странице "Лента заказов" за сегодня')
    def test_up_counter_today_after_order(self, feed_auth):
        before = feed_auth.get_counter_ready_orders_today()
        feed_auth.create_new_order()
        after = feed_auth.get_counter_ready_orders_today()

        assert after > before

    @allure.title('Проверяем номер заказа "В работе"')
    @allure.description('Тест проверяет, что на странице "Лента заказов" в графе "В работе" отображается номер заказа')
    def test_number_order_in_progress(self, feed_auth):
        number = feed_auth.create_new_order()

        assert feed_auth.get_id_order_in_progress() == number

