from data import Urls


class TestLogin:

    def test_click_personal_area_link(self, login_page):

        assert login_page.driver.current_url == Urls.LOGIN_PAGE

    def test_open_history_orders(self, login_auth):
        login_auth.goto_history_orders()

        assert login_auth.driver.current_url == Urls.HISTORY_ORDERS
