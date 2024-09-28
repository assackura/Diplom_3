import pytest

from api.user import User
from data import Urls
from selenium import webdriver
from generators import UserGenerator
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=['firefox'])
#@pytest.fixture(params=['chrome'])
def driver(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise Exception(f"Браузер {request.param} не поддерживается")
    browser.set_window_size(1920, 1080)
    yield browser

    browser.quit()

@pytest.fixture(scope='function')
def new_user_data():
    generator = UserGenerator()
    user_data = {
        "name": generator.generate_random_string(6),
        "email": generator.generate_random_email(),
        "password": generator.generate_random_string(10)
        }
    return user_data

@pytest.fixture(scope='function')
def user_delete_after_test(new_user_data):
    user = User()
    response = user.create_new_user(new_user_data["email"], new_user_data["password"], new_user_data["name"])

    yield response, new_user_data

    user.delete_user(response.json()["accessToken"])

@pytest.fixture(scope='function')
def forgot_page(driver):
    forgot_pwd = ForgotPasswordPage(driver)
    forgot_pwd.open_page(Urls.MAIN_PAGE)
    return forgot_pwd

@pytest.fixture(scope='function')
def fill_email_and_recovery(forgot_page):
    generator = UserGenerator()
    forgot_page.click_recovery_password()
    return forgot_page, generator.generate_random_email()

@pytest.fixture(scope='function')
def login_page(driver):
    login = LoginPage(driver)
    login.open_page(Urls.MAIN_PAGE)
    return login

@pytest.fixture(scope='function')
def login_auth(login_page, user_delete_after_test):
    login_page.login_user(user_delete_after_test[1]["email"], user_delete_after_test[1]["password"])
    return login_page

@pytest.fixture(scope='function')
def main_page(driver):
    main = MainPage(driver)
    main.open_page(Urls.MAIN_PAGE)
    return main

@pytest.fixture(scope='function')
def main_auth(main_page, user_delete_after_test):
    main_page.login_user(user_delete_after_test[1]["email"], user_delete_after_test[1]["password"])
    return main_page

@pytest.fixture(scope='function')
def feed_page(driver):
    feed = FeedPage(driver)
    feed.open_page(Urls.MAIN_PAGE)
    return feed

@pytest.fixture(scope='function')
def feed_auth(feed_page, user_delete_after_test):
    feed_page.login_user(user_delete_after_test[1]["email"], user_delete_after_test[1]["password"])
    return feed_page