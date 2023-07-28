from flask import Flask
from flask_migrate import Migrate

from models.models import db

from urls.urls_app import app_urls

app = Flask(__name__)
app.register_blueprint(app_urls)
app.config.from_object("settings.config.Config")
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
