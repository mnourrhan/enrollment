from flask import Flask, Blueprint
from config import Config
from flask_mongoengine import MongoEngine
from flask_restplus import Api

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

blueprint = Blueprint('api',__name__,url_prefix='/restful')
api = Api(blueprint, doc='/doc/')
app.register_blueprint(blueprint)
# api.init_app(app)

from application import routes
