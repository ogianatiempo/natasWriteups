def read_passwords(file):
    """
    Esta funcion crea un diccionario con las credenciales de cada nivel a partir de un archivo.
    Ver el archivo modelo natas_passwords_sample.
    """
    credentials = {}

    for line in open(file, 'r'):
        line = ''.join(line.split())

        data = [element.replace('\n', '') for element in line.split(':')]
        data = [''.join(element.split()) for element in data]
        credentials[data[0]] = data[1]

    return credentials