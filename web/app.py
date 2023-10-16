"""
Dylan Murphy's Flask API.
"""

from flask import Flask
import os
import configparser

#config parser for credentials file
def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])
sPort = config["SERVER"]["PORT"]
print(sPort)
dBug = config["SERVER"]["DEBUG"]
print(dBug)


app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"
@app.route("/trivia.html")
def trivia():
    return "Tar Pit Surf Co.\n"


if __name__ == "__main__":
    app.run(debug=dBug, host='0.0.0.0', port=sPort)
