from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS

import json

from src.routes.sampleExternalRoutes import SampleRoutes

app = Flask(__name__)
CORS(app)

app.register_blueprint(SampleRoutes, url_prefix="/sample")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/jsonEndpoint/")
def statusRoute():
    return jsonify({"Sample Json": True})


@app.route("/dynamicRouteVariable/<string:name>/")
def dynamicRouteVariable(name: str):
    return jsonify({"name": name})


@app.route("/bodyParams/", methods=['POST', 'GET'])
def bodyParams():
    body = dict(request.form)
    cookies = dict(request.cookies)

    return jsonify({
        "method": request.method,
        "body": body,
        "cookies": cookies
    })


@app.route("/redirect/")
def redirectRoute():
    return redirect("/")


if __name__ == "__main__":
    with open("config.json") as file:
        config = json.load(file)

    app.run(port=config['port'], debug=True)
