# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from services.scheduller_service import SchedulerService

app = Flask(__name__)

ss = SchedulerService()
ss.start()

@app.route("/")
def health():
    try:
        return jsonify(message='The Server is OK!')
    except Exception as e:
        return jsonify(message='Error Server is down!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
