# -*- coding: utf-8 -*-

from flask import Flask, url_for, request
app = Flask('teste')

@app.route('/')
def grupython():
	return '<h1>Grupython</h1>'
	
@app.route('/hello')
def hello():
	return '<h1>Hello</h1>'
	
@app.route('/user/<username>')
def show_user(username):
	return 'User {nome}'.format(nome=username)
	
@app.route('/post/<int:post_id>')
def show_id(post_id):
	return 'Post {numero}'.format(numero=post_id+3)

@app.route('/hello/')
def hello_slashes():
	return '<h1>Hello Project</h1>'
	
@app.route('/print')
def printfunction():
	return '<a href='+url_for('show_user',username='Thiago')+'><h1>Nome</h1></a>'

@app.route('/test', methods=['GET', 'POST'])
def test():
	form = '''
		<form method='POST'>
			<input type='text' name='nome' placeholder='Nome'/>
			<input type='submit' value='Clique aqui' />
		</form>
	'''
	if request.method == 'GET':
		return form
	else:
		return 'Welcome ' + request.values['nome']


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)

