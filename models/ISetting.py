from hashlib import sha256
import os.path
from abc import ABCMeta, abstractmethod

class ISetting(object):
    __metaclass__ = ABCMeta

    address = ''
    port = 1927

    @abstractmethod
    def check(self):
        pass
    
    

class ServerConnection(ISetting):
    address = '127.0.0.1'
    port = 1927

    def check(self):
        pass

class SQLConnection(ISetting):
    address = '127.0.0.1'
    port = 1433

    def check(self):
        pass