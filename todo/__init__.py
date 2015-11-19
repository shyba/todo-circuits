#!/usr/bin/env python

import os
from json import loads
from circuits.web import Server, JSONController

METHODS = 'POST, HEAD, GET, OPTIONS, DELETE'


CORS_HEADERS = {}
CORS_HEADERS["Access-Control-Allow-Origin"] = "*"
CORS_HEADERS['Access-Control-Allow-Methods'] = METHODS
CORS_HEADERS["Access-Control-Allow-Headers"] = "Content-Type"


def json_parser(f):
    def wrapper(self, *args, **kwargs):
        self.request.body = loads(self.request.body.read().decode())
        return f(self, *args, **kwargs)
    return wrapper


class Root(JSONController):

    def _set_CORS(self):
        self.response.headers.update(CORS_HEADERS)

    def index(self):
        self._set_CORS()
        return []

    def OPTIONS(self):
        self.response.headers['Allow'] = METHODS
        self._set_CORS()

    @json_parser
    def POST(self):
        return self.request.body


def run():
    port = os.environ.get("PORT", 8000)
    app = Server(("0.0.0.0", int(port)))
    Root().register(app)
    app.run()
