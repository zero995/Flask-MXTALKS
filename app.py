# coding=utf-8
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

hello_msg = 'Hello, nice to meet you'


@app.route('/hello world')
def hello():
    return 'Hello World from Python Flask!'


@app.route('/get_url/<string:name>', methods=['GET'])
def get_read(name):
    return hello_msg + " " + name


@app.route('/multi', methods=['GET', 'POST'])
def multi():
    if request.method == 'POST':
        name = request.form.get('name', None)

    elif request.method == 'GET':
        name = request.args.get('name', None)

    if name is not None:
        name = " " + name
    else:
        name = ""

    if request.method == 'POST':
        return jsonify({'say_hello': hello_msg + name})
    elif request.method == 'GET':
        return hello_msg + name


@app.route('/basic', methods=['GET'])
def basic_html():
    users = [
        {"name": "zero", "url": "http://localhost"},
        {"name": "exe", "url": "http://localhost"},
        {"name": "test", "url": "http://localhost"},
    ]
    return render_template("basic.html", users=users)


@app.route('/render', methods=['GET'])
def example_dash():
    return render_template("index.html")


if __name__ == '__main__':
    app.env = "development"
    app.run(port=3000, host="0.0.0.0", debug=True)
