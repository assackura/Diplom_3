import configparser

class GetConfig:

    @staticmethod
    def get_conf(head, param):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        return config[head][param]

class Urls:

    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    FORGOT_PASSWORD = f"{MAIN_PAGE}forgot-password"
    RESET_PASSWORD = f"{MAIN_PAGE}reset-password"
    LOGIN_PAGE = f"{MAIN_PAGE}login"
    HISTORY_ORDERS = f"{MAIN_PAGE}account/order-history"

class EndPoints:
    CREATE_USER = "api/auth/register"
    GET_AND_DELETE_USER = "api/auth/user"