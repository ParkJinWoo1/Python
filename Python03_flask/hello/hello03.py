# -*- coding:utf-8 -*-

from flask import Flask, request



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_root():
    html='''
    <h1> Get or Post</h1>
    <a href="/test">get</a>
    <form action="/test" method="post">
        <input type="submit" value="post" />
    </form>
    '''
    return html

@app.route('/test', methods=['GET', 'POST'])
def hello_test():
    if request.method == 'GET':
        return '<h1 style="color: red;">Request Get</h1>'
    elif request.method=='POST':
        return '<h1 style="color: green;">Request Post</h1>'


if __name__ == '__main__':
    app.run()
    
    
    
    
