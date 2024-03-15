import json
from flask import Flask, request,Blueprint,jsonify
from pkg.utils.exp import process_images


exp_api = Blueprint('exp_api', __name__)


@exp_api.route('/exp-api', methods=['POST'])
def detect_dates():
    try:
        # Get file path from request
        image_path = request.json.get('img_path')


        date_info = process_images([image_path])


        return jsonify(date_info)

    except Exception as e:
        return str(e), 500

