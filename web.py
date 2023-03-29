from flask import Flask, render_template, request
import json

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html.jinja2', messages=messages)

@app.route('/submit_message', methods=['POST'])
def submit_message():
    message = request.form['message']
    username = request.form['username']
    messages.append({'发送了': message, '用户名': username})
    with open('messages.json', 'w') as f:
        json.dump(messages, f)
    return '', 204

if __name__ == '__main__':
    app.run()

