# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, Markup, request, redirect
from werkzeug import secure_filename
import os

app = Flask('site_grupython')
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists('uploads/'):
    os.mkdir('uploads')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello(name):
    items = ['banana', '<em>sem markup</em>',
             Markup('<em>com markup</em>')]
    return render_template('hello.html', name=name,
                           items=items)


def valid_login(username, keyword):
    return username == 'Jensen' and keyword == '123'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = ""
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['keyword']):
            return redirect(url_for('hello', name=request.form['username']))
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/test')
def test():
    args = request.args.get('name', '')
    return args


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['the_file']
        file_path = os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(file_path)
        return 'Upload realizado com sucesso!'
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
