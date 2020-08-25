# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


# 앱에 대한 경로
@app.route('/') # decoration == 어노테이션과 같은 개념
def hello():
    return 'Hello, World!'

if __name__=='__main__':
    app.run()