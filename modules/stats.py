import base64

#Data Vars
cpu = 3
ram = 4
disk = 5

class Encryption():
    def encode(self, string):
        code = base64.b64encode(string)
        return code

    def decode(self, string):
        code = base64.b64decode(string)
        return code
