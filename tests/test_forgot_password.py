'''
from data import Urls

class TestForgotPassword:

    def test_goto_page_recovery_password(self, forgot_page):

        assert forgot_page.driver.current_url == Urls.FORGOT_PASSWORD

    def test_fill_email_click_btn_recovery(self, fill_email_and_recovery):

        assert fill_email_and_recovery.driver.current_url == Urls.RESET_PASSWORD

    def test_click_show_hide_password_btn(self, fill_email_and_recovery):

        assert fill_email_and_recovery.click_show_hide_password_btn() == "text"
'''