# Flask Project Template

A basic template and starter guide to making your own simple backend server in Python using the Flask framework.

While not an extensive template or example of all the features of Flask, this should allow a quick start for beginners
and a good starting point for most projects.

All Official documentation can be found at https://flask.palletsprojects.com/en/2.1.x/

## Getting Started / Installation

### (Optional but Recommended) Running in virtual environment

Running in a virtual environment is not necessary, but highly recommended to ensure package version stability per
project

Install virtualenv:

```bash
pip3 install virtualenv
```

Create in folder:

```bash
virtualenv env
```

Activate virtual env

```bash
venv/scripts/activate
```

Install by running a pip install in the given requirements file:

```bash
pip3 -r requirements.txt
```

## Running Development / Production

You can rnn the server in a development environment by running

```bash
python3 App.py
```

This will allow you to simply run the app with logging and a debugging

You can run the app in production by running:

```bash
python3 __init__.py
```

which will allow multiple clients to safely send requests to the application and turn off extensive logging and
debugging.

Running the project will automatically start the server at http://localhost:8080/, however you can modify the port
number in "config.json".
