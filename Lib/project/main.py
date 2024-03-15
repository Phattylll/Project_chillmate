from flask import Flask
from flask_cors import CORS  
from api.exp_api import exp_api
from api.obj_api import obj_api
from pkg.env import PORT

app = Flask(__name__)


CORS(app)

app.register_blueprint(exp_api)
app.register_blueprint(obj_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True)