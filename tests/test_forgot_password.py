class TestForgotPassword:

    def test_goto_page_recovery_password(self, forgot_page):

        assert forgot_page.click_recovery_password().is_displayed()

    def test_fill_email_click_btn_recovery(self, fill_email_and_recovery):

        assert fill_email_and_recovery[0].fill_email_and_click_recovery(fill_email_and_recovery[1]).is_displayed()

    def test_click_show_hide_password_btn(self, fill_email_and_recovery):
        fill_email_and_recovery[0].fill_email_and_click_recovery(fill_email_and_recovery[1])

        assert fill_email_and_recovery[0].click_show_hide_password_btn() == "text"
