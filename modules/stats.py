import base64

#Vars
cpuBool  = True
ramBool  = False
ttuValue = 2.00

#ID Vars
cpu  = 1
ram  = 2
ttu  = 3

def GetState(type):
    if(type == "cpu"):
        if(cpuBool == True):  return "T"
        else:         return "F"
    if(type == "ram"):
        if(ramBool == True):  return "T"
        else:         return "F"
    if(type == "ttu"):
        return ttuValue

class Encryption():
    def encode(self, string):
        code = base64.b64encode(string)
        return code

    def decode(self, string):
        code = base64.b64decode(string)
        return code
