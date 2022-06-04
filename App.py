from flask import Flask, jsonify, request, render_template, redirect, send_from_directory
from flask_cors import CORS

import json

from src.routes.sampleExternalRoutes import SampleRoutes

app = Flask(__name__)

# Enables CORS on our application
CORS(app)

# Example of using an external file for holding routes. URL prefix is optional
app.register_blueprint(SampleRoutes, url_prefix="/sample")

'''
Index route

All routes are basic python functions with an @app.route() decorator with a routing name as the parameter

Returning a "render_template" instead of just a file object will allow the browser to display the html file correctly as a file
'''
@app.route("/")
def index():
    return render_template('index.html')


'''
Example Serving static files
'''
@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

'''
Example JSON endpoint

Returning a jsonify function will allow us to transform a dictionary into a json object with all the correct json headers
'''
@app.route("/jsonEndpoint/")
def statusRoute():
    return jsonify({"Sample Json": True})


'''
Example of getting a variable from the url. You can also pass in integers, doubles, or booleans
'''
@app.route("/dynamicRouteVariable/<string:name>/")
def dynamicRouteVariable(name: str):
    return jsonify({"name": name})


'''
Example of getting data from the request object. Aall the incoming request data can be accessed through the request object.

Accessing specific body/cookie data can be gotten through request.form.get("KEY") or request.cookies.get("KEY")

'''
@app.route("/bodyParams/", methods=['POST', 'GET'])
def bodyParams():
    body = dict(request.form)
    cookies = dict(request.cookies)

    return jsonify({
        "statusCode": request.headers,
        "method": request.method,
        "body": body,
        "cookies": cookies
    })


'''
Example Redirect
'''
@app.route("/redirect/")
def redirectRoute():
    return redirect("/")


if __name__ == "__main__":
    with open("config.json") as file:
        config = json.load(file)

    app.run(port=config['port'], debug=True)
