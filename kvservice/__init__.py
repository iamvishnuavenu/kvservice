from kvservice.db import get_db
from kvservice.kv_store import KVStore
import os
from flask import Flask, request, jsonify

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'kv.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    MAIN_ROUTE = "/api/vi/resource/kv/"

    # def process_args(args):



    @app.route(MAIN_ROUTE, methods=["GET", "POST", "DELETE"])
    def process_request():
        if request.method == "GET":
            result = {}
            if 'key' in request.args.keys():
                for val in request.args.getlist('key'):
                    try:
                        result[val] = db.get_db()[val]
                    except KeyError:
                        return "Error: No such key stored. Please check key."           
            else:
                for k in get_db().items():
                    result[k[0]] =  k[1]
            return jsonify(result)

        elif request.method == "POST":
            print(request.args.to_dict())
            for key in request.args.to_dict():
                get_db()[key] = request.args.to_dict()[key]
            return jsonify(request.args.to_dict())

        elif request.method == "DELETE":
            if 'key' in request.args.keys():
                for key in request.args.getlist('key'):
                    try:
                        del get_db()[key]
                        return { "key": key}
                    except KeyError:
                        return "Error: Key Deletion failed. Key Doesnt exist"
        
    return app
