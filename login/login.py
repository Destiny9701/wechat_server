# __author:"Destiny"
# date: 2018/1/13
import os
import re
import sqlite3

from verify import yzm

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(CURRENT_PATH, "User.db")


class Login:
    def __init__(self, uuid):
        self.is_login = False
        self.__uuid = uuid
        self.__verify = None
        self.__pwd = None

    def login(self, name, pwd, verify_code):
        if len(name) > 12 or len(pwd) > 18 or len(verify_code) > 4:
            return False, '4008'
        if self.__re_check(name) or self.__re_check(pwd):
            return False, '4005'
        if verify_code != self.__verify:
            return False, '4002'
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''select password from user where name = ?''', (name,))
        try:
            self.__pwd = cursor.fetchall()[0][0]
        except Exception:
            return False, '4003'
        finally:
            cursor.close()
            conn.close()
        if pwd == self.__pwd:
            return True, '4000'
        else:
            return False, '4001'
        pass

    def register(self, name, pwd, verify_code, nickname="盒子"):

        if len(name) > 12 or len(pwd) > 18 or len(verify_code) > 4:
            return False, '4008'
        if self.__re_check(name) or self.__re_check(pwd):
            return False, '4005'
        if self.__verify != verify_code:
            return False, '4002'
        if not self.__check_name(name):
            return False, '4006'
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''insert into user (name, password, nickname, uuid)\
        values(?,?,?,?)\
        ''', (name, pwd, nickname, self.__uuid))
        conn.commit()
        cursor.close()
        conn.close()
        return True, '4000'

    def get_verify_img(self):
        if self.__uuid:
            self.__verify = yzm.generate_verification_code(self.__uuid)
        else:
            raise ValueError("uuid不存在，请检查!")

        pass

    def get_nickname(self, name):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''select nickname from user where name =?''', (name,))
        nickname = cursor.fetchall()[0][0]
        cursor.close()
        conn.close()
        return nickname

    def __check_name(self, name):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''select name from user''')
        names = cursor.fetchall()
        cursor.close()
        conn.close()
        if (name,) in names:
            return False
        else:
            return True

    def __re_check(self, string):
        if re.search("\W", string):
            return True
        else:
            return False


if __name__ == "__main__":
    pass
