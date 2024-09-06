from flask import Blueprint, request, session, redirect, url_for, send_file
from models.user_model import random_color
from PIL import Image
import io

image_blueprint = Blueprint('image', __name__)

@image_blueprint.route('/image')
def image():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    try:
        width = int(request.args.get('width', 100))
        height = int(request.args.get('height', 100))
        image = Image.new('RGB', (width, height), random_color())
        byte_io = io.BytesIO()
        image.save(byte_io, 'PNG')
        byte_io.seek(0)
        return send_file(byte_io, mimetype='image/png')
    except Exception as e:
        return str(e), 400
