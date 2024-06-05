

from flask import Flask
from blueprints.about.route import about
from blueprints.home.route import home
from blueprints.teste.route import teste
# Import other blueprints

def create_app():
    app = Flask(__name__)


    # Register blueprints
    app.register_blueprint(home)
    app.register_blueprint(about)
    app.register_blueprint(teste)

    # Register other blueprints
    return (app)

