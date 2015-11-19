#!/usr/bin/env python

import os
from circuits.web import Server, JSONController

METHODS = 'POST, HEAD, GET, OPTIONS, DELETE'


CORS_HEADERS = {}
CORS_HEADERS["Access-Control-Allow-Origin"] = "*"
CORS_HEADERS['Access-Control-Allow-Methods'] = METHODS
CORS_HEADERS["Access-Control-Allow-Headers"] = "Content-Type"


class Root(JSONController):

    def _set_CORS(self):
        self.response.headers.update(CORS_HEADERS)

    def index(self):
        self._set_CORS()
        return []

    def OPTIONS(self):
        self.response.headers['Allow'] = METHODS
        self._set_CORS()

    def POST(self, **args):
        return args


def run():
    port = os.environ.get("PORT", 8000)
    app = Server(("0.0.0.0", int(port)))
    Root().register(app)
    app.run()
