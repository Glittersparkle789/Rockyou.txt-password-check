from flask import Flask, render_template, request
import os

app = Flask(__name__)

with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
    weak_passwords = set(f.read().splitlines())

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', result=None)

@app.route('/check', methods=['POST'])
def check_password():
    password = request.form['password']
    if password in weak_passwords:
        result = "Your password is not safe"
    else:
        result = "Your password is safe"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)