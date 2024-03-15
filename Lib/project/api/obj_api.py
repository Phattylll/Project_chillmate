from flask import Flask, jsonify, request,Blueprint
from pkg.utils.obj import predict_class
obj_api = Blueprint('obj_api', __name__)

@obj_api.route('/obj-api', methods=['POST'])
def predict():
    try:
  
        data = request.get_json()
        img_path = data.get('img_path')

   
        result = predict_class(img_path)

    
        response = {'class': result}

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

