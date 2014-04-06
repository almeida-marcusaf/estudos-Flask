from flask.ext.script import Manager, Shell
from encontro_05_04_2014 import app

manager = Manager(app)


@manager.command
def hello():
    '''
        Imprime hello na tela marolo.
    '''
    print "hello"


def admin_context():
    return {'db': 'o banco', 'admin': 'auth'}


@manager.command
def teste():
    a = Shell(banner='custom shell', make_context=admin_context,
              use_ipython=True)
    a.run(False, False)

manager.add_command("shell_custom", Shell(
    banner='custom shell', make_context=admin_context))

if __name__ == "__main__":
    manager.run()
