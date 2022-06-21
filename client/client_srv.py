from datetime import datetime
from distutils.log import INFO
from flask import Flask
from flask_restful import Api
from apscheduler.schedulers.background import BackgroundScheduler
from resources.clients import Clients
import json
import logging
import sys
import requests


app = Flask(__name__)
api = Api(app)

def load_config(file_path):
    logging.basicConfig(filename='log.txt', filemode='w', level=INFO)
    with open(file_path, "r") as f:
        return json.load(f)

config = load_config("config.json")

client_ip = str(sys.argv[1])
client_port = int(sys.argv[2])

def publish_time_to_server():
    params = {'time': str(datetime.now()), 'client_ip': client_ip, 'port': client_port}
    logging.info(params)
    res = requests.post(config["server_url"], json=params)
    time = params['time']

    if not res.ok:
        logging.warning(f'failed publishing time to master {time}')


scheduler = BackgroundScheduler()
scheduler.add_job(publish_time_to_server, 'interval', seconds=1)
scheduler.start()

api.add_resource(Clients, '/time')
app.run(host=client_ip, port=client_port)
