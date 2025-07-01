# El módulo requests es la solución estándar de facto para realizar peticiones HTTP en Python. 
# Su API, elegante y sencilla, permite interactuar con servicios web y APIs de una manera muy intuitiva, 
# eliminando la complejidad del trabajo con sockets y la codificación de datos.

import requests

# Realizar una petición GET a una API
response = requests.get('https://api.github.com/users/python')

# Comprobar si la petición fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    print("Nombre de usuario:", data['login'])
    print("Número de repositorios públicos:", data['public_repos'])
else:
    print("Error en la petición:", response.status_code)
    
