from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)