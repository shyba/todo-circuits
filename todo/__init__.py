#!/usr/bin/env python

import os
from circuits.web import Server, JSONController


class Root(JSONController):

    def index(self):
        return {"success": True}


def run():
    port = os.environ.get("PORT", 8000)
    app = Server(("0.0.0.0", int(port)))
    Root().register(app)
    app.run()
