from model.user import User
from logger_base import log
from utils.database.cursor_of_pool import CursorOfPool


class UserDAO:
    _SELECT = 'SELECT id_user, username, password FROM PUBLIC.USER ORDER BY id_user ASC'
    _INSERT = 'INSERT INTO PUBLIC.USER ( username, password) VALUES (%s, %s)'
    _UPDATE = 'UPDATE PUBLIC.USER SET username = %s, password = %s WHERE id_user = %s'
    _DELETE= 'DELETE FROM PUBLIC.USER WHERE id_user = %s'

    @classmethod
    def createUser(cls, user: User):
        with CursorOfPool() as cursor:
            values = (user.username, user.password)
            cursor.execute(cls._INSERT, values)
            log.debug(f'Usuario creado: {user}')
            return cursor.rowcount
    @classmethod
    def readUser(cls):
        with CursorOfPool() as cursor:
            cursor.execute(cls._SELECT)
            records = cursor.fetchall()
            userList: [User] = []
            for record in records:
                user = User(record[0], record[1], record[2])
                userList.append(user)
            return userList

    @classmethod
    def updateUser(cls, user: User):
        with CursorOfPool() as cursor:
            values = (user.username, user.password, user.id_user)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'Usuario actualizado: {user}')
            return cursor.rowcount

    @classmethod
    def deleteUser(cls, user: User):
        with CursorOfPool() as cursor:
            values = (user.id_user,)
            cursor.execute(cls._DELETE, values)
            log.debug(f'Usuario eliminado: {user}')
            return cursor.rowcount


if __name__ == '__main__':

    # user = User(name='Manuel', last_name='Garcia', email='mgarcia@mail.com')
    # registers = UserDAO.createUser(user)
    # log.debug(f'Registros creados: {registers}')
    #
    # user = User(name='Pablo', last_name='Prado', email='pprado@mail.com', id_user=2)
    # registers = UserDAO.updateUser(user)
    # log.debug(f'Registros actualizados: {registers}')
    #
    # user = User(id_user=5)
    # registers = UserDAO.deleteUser(user)
    # log.debug(f'Registros eliminados: {registers}')

    userList = UserDAO.readUser()
    for user in userList:
        log.debug(user)

