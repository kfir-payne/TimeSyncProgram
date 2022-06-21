from datetime import datetime

class Client():
    def __init__(self, ip: str, time: datetime, port: int) -> None:
        self._ip = ip
        self._port = port
        self._time = time
    
    def __eq__(self, __o: object) -> bool:
        return self.ip == __o.ip and self.port == __o.port

    @property
    def ip(self):
        return self._ip

    @property
    def port(self):
        return self._port

    @property
    def time(self):
        return self._time
       
    @time.setter
    def time(self, time: datetime):
        self._time = time