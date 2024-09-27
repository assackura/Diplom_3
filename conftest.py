import pytest

from api.user import User
from data import Urls
from selenium import webdriver
from generators import UserGenerator
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


#@pytest.fixture(params=['firefox', 'chrome'])
@pytest.fixture(params=['chrome'])
def driver(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise Exception(f"Браузер {request.param} не поддерживается")
    yield browser

    browser.quit()

@pytest.fixture(scope='function')
def forgot_page(driver):
    forgot_pwd = ForgotPasswordPage(driver)
    forgot_pwd.open_page(Urls.MAIN_PAGE)
    forgot_pwd.click_recovery_password()
    return forgot_pwd

@pytest.fixture(scope='function')
def fill_email_and_recovery(forgot_page):
    generator = UserGenerator()
    forgot_page.fill_email_and_click_recovery(generator.generate_random_email())
    return forgot_page

@pytest.fixture(scope='function')
def login_page(driver):
    login = LoginPage(driver)
    login.open_page(Urls.MAIN_PAGE)
    return login

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
def login_auth(login_page, user_delete_after_test):
    login_page.click_personal_area_link()
    login_page.login_user(user_delete_after_test[1]["email"], user_delete_after_test[1]["password"])
    return login_page
