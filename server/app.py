#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return(f'{parameter}')

@app.route('/count/<int:integer>')
def count(integer):
    result = ''
    for num in range(integer):
        result = result +f'{num}\n'
    return result

@app.route('/math/<int:num1>/<opr>/<int:num2>')
def math(num1, opr, num2):
    result = ''
    if opr == '+':
        result = num1 + num2
    elif opr == '-':
        result = num1 - num2
    elif opr == '*':
        result = num1 * num2
    elif opr == 'div':
        result = num1/num2
    elif opr == '%':
        result = num1%num2
    return f'{result}'