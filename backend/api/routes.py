from flask import Blueprint

api = Blueprint('api', __name__)

@api.route("/v1/api", methods=['GET'])
def hello_world():
    return ("Hello World!")