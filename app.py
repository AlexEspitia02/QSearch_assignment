from flask import Flask
from controllers.image_controller import image_blueprint
from controllers.auth_controller import auth_blueprint

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.register_blueprint(image_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
