from flask import Flask
from dotenv import load_dotenv
from controllers.image_controller import image_blueprint
from controllers.auth_controller import auth_blueprint
from controllers.logging_config import setup_logging
import os

load_dotenv()

credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

app = Flask(__name__, static_url_path='/static', static_folder='static')

app.secret_key = os.getenv('SECRET_KEY')

logger = setup_logging(credentials_path)

app.register_blueprint(image_blueprint)
app.register_blueprint(auth_blueprint)

app.logger = logger

if __name__ == '__main__':
    app.logger.info('Application started')
    app.run(debug=True)
