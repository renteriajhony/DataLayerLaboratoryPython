import logging

from dao.user_dao import UserDAO
from model.user import User


class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def get_all_user(self):
        return self.user_dao.readUser()

    def add_user(self, username, password):
        if (username is None or password is None) or (username == '' or password == ''):
            logging.debug(f'Datos incorrectos, datos obligatorios username = ({username}), password = ({password})')
        else:
            self.user_dao.createUser(User(None, username=username, password=password))

    def update_user(self, id_user, username, password):
        if id_user is None or id_user == '':
            logging.debug(f'El campo id_user = ({id_user}) no es valido')
        elif (username is None and password is None) or (username == '' and password == ''):
            logging.debug(f'Datos incorrectos, datos obligatorios username = ({username}), password = ({password})')
        else:
            user = User(id_user= id_user)
            if user.username is not None or user.username != '':
                user.username = username
            if user.password is not None or user.password != '':
                user.password = password
            return self.user_dao.updateUser(user)

    def delete_user(self, id_user):
        if id_user is None or id_user == '':
            logging.debug(f'El campo id_user = ({id_user}) no es valido')
        else:
            return self.user_dao.deleteUser(User(id_user=id_user))