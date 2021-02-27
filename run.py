import firebase_admin
from dotenv import load_dotenv, find_dotenv
from firebase_admin import credentials
from flask import Flask

from app.api.controllers import api
from app.database.sqlalchemy_extension import db
from config import LocalConfig, get_env_config


def create_app(config_env=None) -> Flask:
    app = Flask(__name__)
    if config_env:
        app.config.from_object(config_env)
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = LocalConfig.SQLALCHEMY_DATABASE_URI
    app.url_map.strict_slashes = False

    load_dotenv(find_dotenv())

    """ Download service file from firebase and put it in project root directory """
    cred = credentials.Certificate("google-credentials.json")
    firebase_admin.initialize_app(cred)

    api.init_app(app)
    db.init_app(app)

    return app


config, port = get_env_config().values()
application = create_app(config)


@application.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    application.run(port=port)
