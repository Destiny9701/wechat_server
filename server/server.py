# __author:"Destiny"
# date: 2018/1/14
from flask import Flask, request, send_from_directory
import json

from config import setting
from login import login

app = Flask(__name__)


class HttpServer:
    def __init__(self):
        self.__uuid = None
        self.__login = None

    def server_login(self):
        @app.route('/verify/<uuid>', methods=['GET'])
        def send_verify(uuid):
            self.__uuid = uuid
            self.__login = login.Login(self.__uuid)
            self.__login.get_verify_img()
            return send_from_directory(setting.VERIFY_IMG, "%s.jpg" % self.__uuid, as_attachment=True)

        @app.route('/login', methods=['POST'])
        def api_login():
            try:
                if not self.__login:
                    msg = {"status": "fail", "welcome": setting.ERROR_CODE['4007']}
                status = self.__login.login(request.form['username'], request.form['password'],
                                            verify_code=request.form['verify'].upper())
            except Exception as e:
                msg = {"status": "fail", "welcome": setting.ERROR_CODE[status[1]]}
            else:
                if status[0]:
                    msg = {"status": "success", "welcome": "%s 欢迎您！" %
                                                           self.__login.get_nickname(request.form['username'])}
                    self.__login.get_verify_img()
                else:
                    msg = {"status": "fail", "welcome": setting.ERROR_CODE[status[1]]}
                    self.__login.get_verify_img()
            finally:
                return json.dumps(msg)
            pass

        @app.route('/register', methods=['POST'])
        def api_register():
            try:
                if not self.__login:
                    msg = {"status": "fail", "welcome": setting.ERROR_CODE['4007']}
                status = self.__login.register(
                    request.form['username'],
                    request.form['password'],
                    request.form['verify'].upper(),
                    request.form['username']
                )
            except Exception:
                msg = {'status': 'fail', 'welcome': setting.ERROR_CODE[status[1]]}
            else:
                if status[0]:
                    msg = {'status': 'success', 'welcome': '%s 注册成功!欢迎您!' % request.form['username']}
                    self.__login.get_verify_img()
                else:
                    msg = {'status': 'fail', 'welcome': setting.ERROR_CODE[status[1]]}
                    self.__login.get_verify_img()
            finally:
                return json.dumps(msg)
            pass


if __name__ == "__main__":
    T = HttpServer()
    T.server_login()
    app.run(host=setting.SERVER, port=setting.PORT, debug=True)
    # t = (False, '4002')
    # print(setting.ERROR_CODE[t[1]])
    pass
