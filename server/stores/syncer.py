
from datetime import datetime
import random
from stores.client import Client
from collections import defaultdict


def def_value():
    return "Client not found"

class Syncer():
    __instance = None

    @staticmethod 
    def getInstance():
        if Syncer.__instance == None:
            Syncer()
        return Syncer.__instance

    def __init__(self) -> None:
        self._clients = defaultdict(def_value)
        self._master_client = None
        if Syncer.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Syncer.__instance = self

    @property
    def master_client(self) -> Client:
         return self._master_client

    @property
    def clients(self) -> dict:
         return self._clients

    @master_client.setter
    def time(self, master_client: Client):
        self._master_client = master_client

    def add_client(self, ip: str, port: int, client: Client) -> None:
        self._clients[ip + str(port)] = client
    
    def remove_client(self, client: Client) -> None:
        del self._clients[client.ip + str(client.port)]
        if client == self._master_client:
            self.remove_master()

    def is_client_exist(self, ip: str, port: int) -> bool:
        return ip + str(port) in self._clients.keys()
    
    def remove_master(self) -> None:
        self._master_client = None

    def choose_master(self) -> None:
        if self._master_client:
            return
        if not self._clients:
            return

        self._master_client = random.choice(list(self._clients.values()))

    def update_client_time(self, ip: str, port: int, time: datetime) -> None:
        self._clients[ip + str(port)].time = time
        if self._master_client.ip == ip and self._master_client.port == port:
            self.master_client.time = time
            