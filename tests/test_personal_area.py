from data import Urls


class TestPersonalArea:

    def test_click_personal_area_link(self, login_page):

        assert login_page.click_personal_area_link().is_displayed()

    def test_open_history_orders(self, login_auth):

        assert login_auth.goto_history_orders().get_attribute("aria-current") == "page"

    def test_logout_user(self, login_auth):

        assert login_auth.logout_user().is_displayed()