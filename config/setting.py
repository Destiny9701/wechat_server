# __author:"Destiny"
# date: 2018/1/14
import sqlite3

from login import login
from verify import yzm

SERVER = "0.0.0.0"
PORT = 80
VERIFY_IMG = yzm.IMG_PATH
ERROR_CODE = {
    '4000': '操作正常!',
    '4001': '用户名或密码错误!',
    '4002': '验证码错误!',
    '4003': '服务器错误!',
    '4004': 'uuid错误!',
    '4005': '用户名和密码不能包含特殊字符!',
    '4006': '用户名重复!',
    '4007': '验证码已过期，请刷新验证码!',
    '4008': '非法操作!用户名、密码或验证码长度错误!'
}

def init():
    conn = sqlite3.connect(login.DATABASE, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''create table if not exists user(
    id             INTEGER PRIMARY KEY   autoincrement,\
    name           text                  not null,\
    password       text                  not null,\
    nickname       text                  not null,\
    uuid           text                  not null\
    );''')
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    init()
