#!/usr/bin/python3
"""
import time
from logging.handlers import TimedRotatingFileHandler

from dateutil import parser
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from application.utils.cloud_log_formatter import CloudLogFormatter
from flask import Flask
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
app = Flask(__name__)
CORS(app)

def load_blueprints(app):
    from application.userland.controller import mod_userland
    from application.userland.controllers.domain_controller import mod_userland as domain_module
    from application.userland.controllers.user_controller import mod_userland as user_module
    app.register_blueprint(mod_userland)


def create_app(config_file_location=None):
    app = Flask(__name__, template_folder="templates")

    if config_file_location:
        app.config.from_pyfile(config_file_location, silent=False)
    else:
        # configure it in order -> prod overrides prp overrides dev
        app.config.from_pyfile('../config/dev.cfg', silent=True)
        app.config.from_pyfile('../config/prp.cfg', silent=True)
        app.config.from_pyfile('../config/prod.cfg', silent=False)

    from application.core.db_models import DomainInfo
    db.init_app(app)
    migrate.init_app(app, db)


    # configure logging
    log_format = (
        "[%(asctime)s] %(levelname)s %(remote_addr)s %(request_type)s %(http_version)s %(url)s %(pathname)s rt:%(response_time)s %(message)s")
    log_formatter = CloudLogFormatter(log_format)
    log_file = app.config['LOG_FILE_PATH']
    log_timed_rotating_handler = TimedRotatingFileHandler(log_file, when="midnight")
    log_timed_rotating_handler.setFormatter(log_formatter)
    log_timed_rotating_handler.setLevel(app.config['LOG_LEVEL'])
    app.static_folder = 'static'
    app.logger.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(log_timed_rotating_handler)

    load_blueprints(app)

    @app.template_filter('ctime')
    def epoch_to_datetime(s):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(s)))

    @app.template_filter('datetimeformat')
    def datetime_format(s):
        if s:
            dt = parser.parse(s)
            return dt.strftime('%Y-%m-%d %H:%M:%S')

    return app


"""









from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

# Kısaltılan URL'leri depolamak için bir sözlük
url_store = {}

# Rastgele karakterlerden oluşan bir kısaltma oluşturma fonksiyonu
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def home():
    return "URL Kısaltma Hizmetine Hoş Geldiniz!"


@app.route('/shorten', methods=['POST'])
def shorten_url():
    print(request.get_json())  # Debugging line to see the form data

    # Dynamically find the field that contains the 'long_url' value
    long_url_field = None
    for field in request.form.keys():
        if 'long_url' in field:
            long_url_field = field
            break

    if long_url_field is None:
        return "No 'long_url' field found in the form data.", 400

    long_url = request.form.get(long_url_field)
    short_url = generate_short_url()
    url_store[short_url] = long_url
    return short_url


@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_store.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "Kısaltılmış URL bulunamadı.", 404

if __name__ == '__main__':
    app.run(debug=True)