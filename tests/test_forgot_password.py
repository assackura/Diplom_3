import allure


class TestForgotPassword:

    @allure.title('Проверяем переход на страницу "Восстановление пароля"')
    @allure.description('Тест проверяет переход на страницу "Восстановление пароля"')
    def test_goto_page_recovery_password(self, forgot_page):

        assert forgot_page.click_recovery_password().is_displayed()

    @allure.title('Проверяем ввод почты и клик по кнопке "Восстановить"')
    @allure.description('Тест проверяет заполнение поля "email" и нажатие на кнопку "Восстановить" на странице "Восстановление пароля"')
    def test_fill_email_click_btn_recovery(self, fill_email_and_recovery):

        assert fill_email_and_recovery[0].fill_email_and_click_recovery(fill_email_and_recovery[1]).is_displayed()

    @allure.title('Проверяем кнопку "Показать/Скрыть" пароль')
    @allure.description('Тест проверяет отображается ли пароль при нажатии на кнопку "Показать/Скрыть" пароль')
    def test_click_show_hide_password_btn(self, fill_email_and_recovery):
        fill_email_and_recovery[0].fill_email_and_click_recovery(fill_email_and_recovery[1])

        assert fill_email_and_recovery[0].click_show_hide_password_btn() == "text"
