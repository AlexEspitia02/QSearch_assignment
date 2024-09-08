from flask import Blueprint, request, session, redirect, url_for, send_file, current_app
from models.user_model import random_color
from PIL import Image
import io
import time

image_blueprint = Blueprint('image', __name__)

@image_blueprint.route('/image')
def image():
    logger = current_app.logger
    
    if 'username' not in session:
        logger.warning('Unauthorized access to /image')
        return redirect(url_for('auth.login'))

    start_time = time.time()

    try:
        width = int(request.args.get('width', 100))
        height = int(request.args.get('height', 100))
        
        image = Image.new('RGB', (width, height), random_color())
        byte_io = io.BytesIO()
        image.save(byte_io, 'PNG')
        byte_io.seek(0)
        logger.info(f'Generated image with size: {width}x{height}')
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        if processing_time > 0.7:
            logger.warning(f"Image generation took longer than expected: {processing_time:.4f} seconds")
        else:
            logger.info(f"Image generated in {processing_time:.4f} seconds")
        
        return send_file(byte_io, mimetype='image/png')
    except Exception as e:
        logger.error(f"Error generating image: {e}")
        return str(e), 400
