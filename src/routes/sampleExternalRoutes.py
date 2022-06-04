from flask import Blueprint, request, jsonify, session, redirect

SampleRoutes = Blueprint("sample", __name__)


@SampleRoutes.route("internalRoute")
def internalRoute():
    return jsonify({"Internal route": True})
