#use the Steam API to get players hours played
#display the data in a table
#use the data to create a graph

# import requests
# import json
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

from flask import Flask, request, jsonify

from models.user import User

#set up the API
app = Flask(__name__)

@app.route('/csgoAna')
def get_stats():

    # new_user = User('jdb', 'testIMGstring', 'testURLString', 'now')
    # JSON_user = jsonify.dumps(new_user.__dict__)
    # return JSON_user
    return 'hello world'
    

if __name__ == '__main__' :
    app.run()
