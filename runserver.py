# coding=utf-8
import os

from calm_temple_8514 import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


port = int(os.environ.get("PORT", 5000))

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port)
IOLoop.instance().start()
