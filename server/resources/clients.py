from datetime import datetime
import logging
from flask import request
from flask_restful import Resource

from stores.client import Client
from stores.syncer import Syncer

class Clients(Resource):
    def post(self) -> None:
        json_data = request.get_json()
        client_ip = json_data["client_ip"]
        client_time = datetime.strptime(json_data["time"], '%Y-%m-%d %H:%M:%S.%f')
        client_port = int(json_data["port"])

        syncer = Syncer.getInstance()

        if not syncer.is_client_exist(client_ip, client_port):
            client = Client(client_ip, client_time, client_port)
            syncer.add_client(client_ip, client_port, client)
        else:
            syncer.update_client_time(client_ip, client_port, client_time)
        
        return