#!/usr/bin/python3

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from application.utils.cloud_log_formatter import CloudLogFormatter
from flask import Flask
from flask_cors import CORS

db = SQLAlchemy()
app = Flask(__name__)
migrate = Migrate()




def load_blueprints(app):
    from application.userland.controller import mod_userland
    from application.userland.controllers.link_controller import mod_userland as link_module
    app.register_blueprint(mod_userland)


def create_app(config_file_location=None):
    app = Flask(__name__, template_folder="templates")
    CORS(app, resources={r"/*": {"origins": "*"}})
    if config_file_location:
        app.config.from_pyfile(config_file_location, silent=False)
    else:
        # configure it in order -> prod overrides prp overrides dev
        app.config.from_pyfile('../config/dev.cfg', silent=True)
        app.config.from_pyfile('../config/prp.cfg', silent=True)
        app.config.from_pyfile('../config/prod.cfg', silent=False)

    #from application.core.db_models import DomainInfo
    db.init_app(app)

    migrate.init_app(app, db)
    #with app.app_context():
    #    db.create_all()

    load_blueprints(app)

    return app

"""
def redirectToLink(uniqueCode: str):
    if checkUniqueCodeValidity(uniqueCode):
        Exception('the cod is not available')
        return False




    return redirect('https://www.youtube.com/')


uniqueCode = "123456"

redirectToLink(uniqueCode)
"""""
