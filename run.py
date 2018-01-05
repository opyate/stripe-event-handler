# coding: utf-8

import os
import logging
import flask
import json
from flask import Flask, request, render_template
import handlers
from models import db

app = Flask(__name__)
app.static_folder = "templates"
app.SEND_FILE_MAX_AGE_DEFAULT = 0
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/stripe', methods=['POST'])
def handler():
        event = json.loads(request.data)
        handlers.handle(event)
        return 'OK'


@app.route('/')
def home():
        return render_template('index.html')

if __name__ == '__main__':
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.WARNING)
        app.logger.addHandler(stream_handler)

        app.debug = False

        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
