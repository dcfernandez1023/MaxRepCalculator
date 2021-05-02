from flask import Flask
from routes import index, one_rep_calculator_routes


app = Flask(__name__)


if __name__ == '__main__':
    app.register_blueprint(index.index_blueprint)
    app.register_blueprint(one_rep_calculator_routes.one_rep_calculator_blueprint)
    app.run(host="0.0.0.0")
