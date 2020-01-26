import modules.stats as stats
from stats import Encryption
crypt = Encryption()

def save(button):
    with open('data.crypt', 'wb') as file:
        code = crypt.encode(  "CPU:  " + stats.GetState("cpu") +
                            "\nRAM:  " + stats.GetState("ram") +
                            "\nTTU:  " + str(stats.GetState("ttu")) + "\n")
        file.write(code)

def load(typeOfObject):
    with open('data.crypt', 'rt') as file:
        code = str(file.read())
        decoded = crypt.decode(code)
        #Set the type of object
        if(typeOfObject == 1):  #CPU
            deleteOther = decoded[:-16]
        if(typeOfObject == 2):  #RAM
            deleteOther = decoded[8:-8]
        if(typeOfObject == 3):  #TTU
            deleteOther = decoded[16:]

        #create the output
        if(typeOfObject != 3):
            string = deleteOther.strip("None\n")
            if("T" in string): result = True
            else:              result = False
        else:
            string = deleteOther.strip("None\n")
            result = string[6:]
        return result
