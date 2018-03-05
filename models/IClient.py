from abc import ABCMeta, abstractmethod\

class IClient:
    def __init__(self, id, idLocation, dateStart, MACAddress):
        self.id = id
        self.idLocation = idLocation
        self.dateStart = dateStart
        self.mac = MACAddress
