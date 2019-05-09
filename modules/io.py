def save(object):
    with open('data.txt', 'wb') as file:
        file.write(object)
