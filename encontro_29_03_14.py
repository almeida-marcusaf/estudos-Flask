#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Não façam isso em casa criançada!
from flask import *
import os

app = Flask("teste2")

@app.route('/cookie')
def cookie():
	username = request.cookies.get('username')
	return render_template('index.html')

@app.route('/cookie2')
def cookie2():	
	resp = make_response(render_template('index.html'))
	resp.set_cookie('grupython', 'ufla')
	return resp

@app.route('/oops')
def redirect_errors():
	abort(404)

@app.errorhandler(404)
def page_not_found(erro):
	return render_template('page_not_found.html'), 404

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session.permanent =True
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#app.secret_key = os.urandom(24)

@app.route('/flash')
def flashing():
	flash('flash exibido com sucesso!')
	flash('flash2 exibido com sucesso!')
	app.logger.debug('A value for debugging')
	return render_template('index.html')

if __name__=='__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
