from flask import Flask
from flask_migrate import Migrate
from lib.models import db
from py_term_helpers import star_line, center_string_stars, top_wrap
from ipdb import set_trace

# MAIN UPLOAD
def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config:
        app.config.from_mapping(test_config)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///serato.db'
    app.config["TEMP_FOLDER"] = './temp'
    app.json.compact = False
    migrate = Migrate(app, db)
    db.init_app(app)

    # from lib.routes import flask_app
    # app.register_blueprint(flask_app)

    return app


if __name__ == "__main__":
    port = 5555
    top_wrap(f"Server Running on {port}")
    app = create_app()
    app.run(port=port, debug=True)
