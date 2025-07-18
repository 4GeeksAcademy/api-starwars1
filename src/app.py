from flask import Flask
from database import db
from flask_migrate import Migrate
from routes import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api, url_prefix='/')


@app.route('/')
def index():
    return "¡Bienvenido a la API de Star Wars!", 200


if __name__ == '__main__':
    app.run(debug=True)
