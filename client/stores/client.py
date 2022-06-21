from datetime import datetime
import sys

class Client():
    __instance = None

    @staticmethod 
    def getInstance():
        if Client.__instance == None:
            Client()
        return Client.__instance

    def __init__(self) -> None:
        self._ip = sys.argv[1]
        self._port = sys.argv[2]
        self._master_time = None
        self._master_ip = ""
        if Client.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Client.__instance = self

    @property
    def ip(self) -> str:
        return self._ip

    @property
    def port(self) -> int:
        return self._port

    @property
    def master_time(self) -> datetime:
        return self._master_time

    @property
    def master_ip(self) -> str:
        return self._master_ip
       
    @master_ip.setter
    def master_ip(self, ip: str):
        self._master_ip = ip
       
    @master_time.setter
    def master_time(self, time: datetime):
        self._master_time = time