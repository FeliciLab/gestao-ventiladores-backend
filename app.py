from flask import Flask
from flask_restful import Api
from config.db import initialize_db
from config.routes import initialize_routes
from flask_bcrypt import Bcrypt

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/gestao-de-ventiladores'
}

initialize_db(app)
initialize_routes(api)

app.run()