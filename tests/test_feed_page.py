class TestFeedPage:

    def test_click_order_open_details(self, feed_page):

        assert feed_page.open_modal_first_order().is_displayed()

    def test_displayed_order_history_in_order_feed(self, feed_auth):
        histrory_order = feed_auth.get_order_number_from_history_orders()
        list_orders_feed = feed_auth.get_list_orders_from_order_feed()

        assert histrory_order in list_orders_feed

