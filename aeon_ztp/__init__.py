# Copyright 2014-present, Apstra, Inc. All rights reserved.
#
# This source code is licensed under End User License Agreement found in the
# LICENSE file at http://www.apstra.com/community/eula

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
ma = Marshmallow()
bs = Bootstrap()
csrf = CSRFProtect()


def create_app(conf=None):
    """Acts as an application factory to create and configure a Flask application object
    """
    if not conf:
        conf = 'production'
    app = Flask(__name__)
    app.config.from_object(config[conf])
    db.init_app(app)
    ma.init_app(app)
    bs.init_app(app)
    csrf.init_app(app)
    from aeon_ztp.api.views import api
    from aeon_ztp.web.views import web
    app.register_blueprint(api)
    app.register_blueprint(web)
    csrf.exempt(api)

    @app.before_first_request
    def initialize_database():
        db.create_all()

    return app
