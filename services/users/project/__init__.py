# services/users/project/__init__.py


import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

# instanciando la db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cors = CORS()
migrate = Migrate()  # Nuevo
bcrypt = Bcrypt()


def create_app(script_info=None):

    # instanciando la app
    app = Flask(__name__)

    # estableciendo la configuración
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # preparando la extensión
    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)  # New
    bcrypt.init_app(app)

    # registrar blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    from project.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    # contexto shell para flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
