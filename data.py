from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

class GetConfig:

    @staticmethod
    def get_conf(head, param):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        return config[head][param]

class Urls:

    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    FORGOT_PASSWORD = "https://stellarburgers.nomoreparties.site/forgot-password"
    RESET_PASSWORD = "https://stellarburgers.nomoreparties.site/reset-password"
    LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"
    HISTORY_ORDERS = "https://stellarburgers.nomoreparties.site/account/order-history"

class EndPoints:
    CREATE_USER = "api/auth/register"
    GET_AND_DELETE_USER = "api/auth/user"