from flask import Blueprint, request, jsonify, session, redirect

SampleRoutes = Blueprint("sample", __name__)

'''
Example external route

Notice that the decorator is @SampleRoutes and not @app.route
'''
@SampleRoutes.route("internalRoute")
def internalRoute():
    return jsonify({"Internal route": True})
