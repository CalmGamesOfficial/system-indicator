import modules.stats as stats
from modules.stats import Encryption
crypt = Encryption()

def save():
    with open ('data.crypt', 'wb') as file:
        code = crypt.encode(  "CPU:  " + stats.GetState("cpu") +
                            "\nRAM:  " + stats.GetState("ram") +
                            "\nDISK: " + stats.GetState("disk") + "\n")
        file.write(code)

def load(typeOfObject):
    with open ('data.crypt', 'rt') as file:
        code = str(file.read())
        decoded = crypt.decode(code)
        #Set the type of object
        if(typeOfObject == 1):  #CPU
            deleteOther = decoded[:-16]
        if(typeOfObject == 2):  #RAM
            deleteOther = decoded[8:-8]
        if(typeOfObject == 3):  #DISK
            deleteOther = decoded[16:]
        #create the output
        string = deleteOther.strip("None\n")
        if ("T" in string): result = True
        else:              result = False

        return result
