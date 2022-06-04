from waitress import serve
import requests
import json

from App import app

if __name__ == "__main__":
    with open("config.json") as file:
        config = json.load(file)

    serve(app=app, port=config['port'])
