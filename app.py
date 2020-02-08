#!/usr/bin/env python3
# coding: utf-8

import flask
import textwrap


app = flask.Flask(__name__)


@app.route('/')
def index():
    content = textwrap.dedent('''\
            <html>
              <body>
                hello, world
              </body>
            </html>
        ''')
    return content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)
