from hashlib import sha256
import os.path

class ISetting:
    def __init__(address, port)
    self.address = address
    self.port = port

    def get(self):
        pass
    
    

class ServerConnection(ISetting):
    def __init__(self):
        ISetting.__init__(self, '127.0.0.1', 6268)

class SQLConnection(ISetting):
    def __init__(self):
        ISetting.__init__(self, '127.0.0.1', 1433)