import base64

#Bool Vars
cpuBool  = True
ramBool  = False
diskBool = False

#ID Vars
cpu  = 1
ram  = 2
disk = 3

def GetState(type):
    if(type == "cpu"):
        if(cpuBool == True):  return "T"
        else:         return "F"
    if(type == "ram"):
        if(ramBool == True):  return "T"
        else:         return "F"
    if(type == "disk"):
        if(diskBool == True): return "T"
        else:         return "F"

class Encryption():
    def encode(self, string):
        code = base64.b64encode(string)
        return code

    def decode(self, string):
        code = base64.b64decode(string)
        return code
