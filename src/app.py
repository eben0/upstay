# The main Flask app
from flask import Flask

from lib.logger import Logger

from routes.api import api_bp
from routes.home import home_bp
from lib.config import Config

try:
    # create logger
    config = Config.instance().all()
    Logger.setup()

    app = Flask(__name__)
    app.logger.info("Starting application...")
    app.config.update(config)

    # registering blueprints
    app.logger.debug("Registering home blueprint...")
    app.register_blueprint(home_bp)
    app.logger.debug("Registering API blueprint...")
    app.register_blueprint(api_bp)

    app.logger.info("application is running now")
except BaseException as e:
    print("Oopsie, there seem be a problem:")
    print(e)
