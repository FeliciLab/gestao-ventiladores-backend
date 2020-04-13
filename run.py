from flask import Flask
from flask_restful import Api
from config.routes import initialize_routes
from flask_mongoengine import MongoEngine
from env_config import mongodb_host
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
CORS(app)

api = Api(app)

DB_URI = mongodb_host

app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')