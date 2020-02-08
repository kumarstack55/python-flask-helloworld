#!/usr/bin/env python
# coding: utf-8

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return '<html><body>hello, world</body></html>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)
