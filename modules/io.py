import modules.stats as stats
from modules.stats import Encryption
crypt = Encryption()

def save():
    with open ('data.crypt', 'w') as file:
        code = (  "CPU:  " + stats.GetState("cpu") +
                            "\nRAM:  " + stats.GetState("ram") +
                            "\nDISK: " + stats.GetState("disk") + "\n")
        file.write(code)

def load(typeOfObject):
    with open ('data.crypt', 'r') as file:
        code = str(file.read())
        #decoded = crypt.decode(code)
        #Set the type of object
        if(typeOfObject == 1):  #CPU
            deleteOther = code[:-16]
        if(typeOfObject == 2):  #RAM
            deleteOther = code[8:-8]
        if(typeOfObject == 3):  #DISK
            deleteOther = code[16:]
        #create the output
        string = deleteOther.strip("None\n")
        if ("T" in string): result = True
        else:              result = False

        return result
