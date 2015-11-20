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


def cors(f):
    def wrapper(self, *args, **kwargs):
        self.response.headers.update(CORS_HEADERS)
        return f(self, *args, **kwargs)
    return wrapper


class Root(JSONController):

    @cors
    def index(self):
        return []

    @cors
    def OPTIONS(self):
        self.response.headers['Allow'] = METHODS

    @cors
    @json_parser
    def POST(self):
        return self.request.body


def run():
    port = os.environ.get("PORT", 8000)
    app = Server(("0.0.0.0", int(port)))
    Root().register(app)
    app.run()
