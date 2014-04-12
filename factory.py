from flask import Flask
from blueprint import simple_page


def create_app(config_filename, name=__name__):
    app = Flask(name)
    app.register_blueprint(simple_page)
    app.config.from_pyfile(config_filename)
    return app
