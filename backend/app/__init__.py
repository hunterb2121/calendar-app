from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .routes.auth_routes import auth_bp
    from .routes.event_routes import event_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(event_bp, url_prefix='/events')

    return app