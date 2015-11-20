#!/usr/bin/env python

import os
from json import loads
from circuits.web import Server, JSONController
from todo import db

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
    def index(self, *args, **kwargs):
        if not args:
            return db.get_all()
        else:
            host = self.request.uri.relative('/').unicode()
            item = args[0]
            return db.get_by_url(host + item)

    @cors
    def OPTIONS(self, *args, **kwargs):
        self.response.headers['Allow'] = METHODS

    @cors
    @json_parser
    def POST(self):
        host = self.request.uri.relative('/').unicode()
        return db.create(self.request.body, host=host)

    @cors
    def DELETE(self):
        db.delete_all()
        return []


def run():
    port = os.environ.get("PORT", 8000)
    app = Server(("0.0.0.0", int(port)))
    Root().register(app)
    app.run()
