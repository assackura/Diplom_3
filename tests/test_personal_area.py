import allure


class TestPersonalArea:

    @allure.title('Проверяем переход на страницу "Личный кабинет"')
    @allure.description('Тест проверяет, что по клику на кнопку "Личный кабинет" происходи переход в личный кабинет')
    def test_click_personal_area_link(self, login_page):

        assert login_page.click_personal_area_link().is_displayed()

    @allure.title('Проверяем открытие истории заказов')
    @allure.description('Тест проверяет, что по нажатию на кнопку "История заказов" происходит переход в '
                        'историю заказов')
    def test_open_history_orders(self, login_auth):

        assert login_auth.goto_history_orders().get_attribute("aria-current") == "page"

    @allure.title('Проверяем выход из аккаунта')
    @allure.description('Тест проверяет выход из аккаунта по нажатию на кнопку')
    def test_logout_user(self, login_auth):

        assert login_auth.logout_user().is_displayed()