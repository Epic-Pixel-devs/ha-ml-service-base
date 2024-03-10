# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import pymongo
app = Flask(__name__)
client = pymongo.MongoClient('mongodb+srv://herdeiros_aurora:herdeiros_aurora_001@cluster0.otugy2g.mongodb.net/')
database = client['dev_ml_IAservice_DC_db']
database = client['dev_ml_IA_NM']

@app.route("/")
def health():
    try:
        return jsonify(message='The Server is OK!')
    except Exception as e:
        return jsonify(message='Error Server is down!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
