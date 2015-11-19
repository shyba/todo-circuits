#!/usr/bin/env python

import os
from circuits.web import Server, JSONController


class Root(JSONController):

    def _set_CORS(self):
        self.response.headers["Access-Control-Allow-Origin"] = "*"

    def index(self):
        self._set_CORS()
        return {"success": True}


def run():
    port = os.environ.get("PORT", 8000)
    app = Server(("0.0.0.0", int(port)))
    Root().register(app)
    app.run()
