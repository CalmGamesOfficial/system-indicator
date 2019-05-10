from modules.stats import Encryption
crypt = Encryption()

def save(object):
    with open('data.crypt', 'wb') as file:
        code = crypt.encode(object)
        file.write(code)

def load(line):
    with open('data.crypt', 'rt') as file:
        code = str(file.readline())
        decoded = crypt.decode(code)
        return decoded
