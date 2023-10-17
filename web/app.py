"""
Dylan Murphy's Flask API.
"""

from flask import Flask, abort, send_from_directory
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


@app.route("/<string:pName>")
def pathname(pName):
        #loop through to look for forbidden characters
        illegal = 0
        for i in range(len(pName)):  # for loop to go through each character
            if pName[i] == '~':
                illegal += 1
            if pName[i] == '.' and (i < len(pName) and pName[i+1] == '.'): # check for '..'
                illegal += 1
                break
            #if illegal transmit error code 403
            if illegal:
                abort(403)
            else:
                #If none found, see if the address entered has a corresponding file
                path = "./pages" + pName
                if os.path.exists(path):
                    return send_from_directory('pages/', pName), 200
                else:
                    abort(404)

@app.errorhandler(403)
def forbidden(e):
   return send_from_directory('pages/', '403.html'), 403
@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory('pages/', '404.html'), 404       


if __name__ == "__main__":
    app.run(debug=dBug, host='0.0.0.0', port=sPort)
