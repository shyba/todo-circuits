#!/usr/bin/env python

import os
from circuits.web import Server, JSONController


class Root(JSONController):
    METHODS = 'POST, HEAD, GET, OPTIONS, DELETE'

    def _set_CORS(self):
        self.response.headers["Access-Control-Allow-Origin"] = "*"
        self.response.headers['Access-Control-Allow-Methods'] = self.METHODS
        self.response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    def index(self):
        self._set_CORS()
        return []

    def OPTIONS(self):
        self.response.headers['Allow'] = self.METHODS
        self._set_CORS()


def run():
    port = os.environ.get("PORT", 8000)
    app = Server(("0.0.0.0", int(port)))
    Root().register(app)
    app.run()
