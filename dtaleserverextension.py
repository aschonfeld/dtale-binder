from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the flask-app directory with D-Tale flask server"""
    Popen(["python", "./dtale-app/main.py"])

