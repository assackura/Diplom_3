class TestMainPage:

    def test_click_constructor(self, main_page):

        assert main_page.constructor_click().is_displayed()

    def test_click_order_feed(self, main_page):

        assert main_page.order_feed_click().is_displayed()

    def test_click_ing_open_window_details(self, main_page):

        assert main_page.click_ing_bun().is_displayed()

    def test_closed_window_detail_ing_click_x(self, main_page):

        assert not main_page.click_closed_detail_window_ing().is_displayed()

    def test_up_counter_ing_add_ing(self, main_page):

        assert int(main_page.add_ing().text) > 0

    def test_auth_user_create_new_order(self, main_page):

        assert main_page.create_new_order().is_displayed()

