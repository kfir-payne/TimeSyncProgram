from datetime import datetime, timedelta
from distutils.debug import DEBUG
from distutils.log import ERROR, INFO
import json
import requests
import logging
from flask import Flask, request
from flask_restful import Api
from resources.clients import Clients
from apscheduler.schedulers.background import BackgroundScheduler
from stores.syncer import Syncer

app = Flask(__name__)
api = Api(app)


def load_config(file_path):
    logging.basicConfig(filename='log.txt', filemode='w', level=logging.WARNING)
    with open(file_path, "r") as f:
        return json.load(f)

config = load_config("config.json")
        
def publish_time_to_clients():
    syncer = Syncer.getInstance()
    syncer.choose_master()
    clients = syncer.clients
    logging.error(str(syncer.master_client.port))

    for client in clients.values():
        url = f'http://{client.ip}:{client.port}/{config["clients_path"]}'
        params = {'master_time': str(syncer.master_client.time), 'master_ip': syncer.master_client.ip}

        try:
            res = requests.post(url, json=params)
            if not res.ok:
                logging.warning(f'failed publishing master time to {client.ip} {res.status_code}')
        except:
            logging.warning(f'failed publishing master time to {client.ip}')

def check_master():
    syncer = Syncer.getInstance()
    master_time = syncer.master_client.time
    if master_time + timedelta(minutes=1) < datetime.now():
        syncer.remove_client(syncer.master_client)
        syncer.master_client = None
        syncer.choose_master()

scheduler = BackgroundScheduler()
scheduler.add_job(publish_time_to_clients, 'interval', seconds=1)
scheduler.add_job(check_master, 'interval', seconds=30)
scheduler.start()

api.add_resource(Clients, '/publish_time')

app.run(host=config["host"], port=config["port"])