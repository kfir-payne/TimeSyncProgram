from datetime import datetime
from doctest import master
from flask import request
from flask_restful import Resource
from stores.client import Client

class Clients(Resource):
    def post(self) -> None:
        json_data = request.get_json()
        master_time = datetime.strptime(json_data["master_time"], '%Y-%m-%d %H:%M:%S.%f')
        master_ip = json_data["master_ip"]

        client = Client.getInstance()
        client.master_time = master_time
        client.master_ip = master_ip