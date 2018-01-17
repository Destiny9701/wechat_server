#__author:"Destiny"
#date: 2018/1/17

from server import server


def main():
    api = server.HttpServer()
    api.server_login()
    api.articles()


main()
