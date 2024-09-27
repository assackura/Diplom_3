class TestOrderFeed:

    def test_click_order_in_order_feed(self, feed_page):

        assert feed_page.open_modal_first_order().is_displayed()
