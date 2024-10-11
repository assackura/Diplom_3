import allure

from api.base import Base
from data import EndPoints


class User(Base):

    @allure.step('Создаем нового пользователя {email}')
    def create_new_user(self, email=None, password=None, name=None):
        body_parametrs = {}
        if email != None:
            body_parametrs["email"] = email
        if password != None:
            body_parametrs["password"] = password
        if name != None:
            body_parametrs["name"] = name
        response = self.post_method(EndPoints.CREATE_USER, None, body_parametrs)
        return response

    @allure.step('Удаляем пользователя')
    def delete_user(self, token):
        headers = {
            "Authorization": f"{token}"
        }
        response = self.delete_method(EndPoints.GET_AND_DELETE_USER, headers, None)
        return response