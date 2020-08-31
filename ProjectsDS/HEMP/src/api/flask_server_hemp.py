import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json
import pandas as pd                                                                 #@Elsa TH
from modulo_api_hemp import rochi
# Creamos la api:

app = Flask(__name__)  

@app.route("/")  
def default():

    return "<h1> API ROCHI</h1>  <h3>Para obtener tu token usa este endpoint: /get_token?=id </h3>"
# Creamos primera función GET
@app.route('/get_token/', methods=['GET'])
def give_id():
    x = request.args['id']
    S =('YB3240290')  #letra grupo + suma de las edades del grupo
    if x == S :
        return {"token": S }
    else:
        return "This is a message of error. Try again."


# Creamos segunda función GET
@app.route('/get_data/', methods=['GET'])
def api_all():
    y = request.args['id']
    
    if y == "YB3240290":
        loqretorna = rochi(url="https://raw.githubusercontent.com/JimKing100/strains-live/master/data/cannabis.csv")
        # data = pd.read_json( "url.ipnb", líneas = True )
        return    loqretorna.to_json()         
    else:
        return "This is a message of error. Try again."




def main():

    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # Get the settings fullpath
    settings_file = os.path.dirname(__file__) + "/settings.json"
    # Load json from file 
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()