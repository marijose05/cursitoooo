# NumPy (Numerical Python) es el pilar fundamental para el cálculo numérico en Python. Su principal objeto es el ndarray 
# (n-dimensional array), una estructura de datos homogénea y multidimensional que permite realizar operaciones matemáticas 
# complejas de manera mucho más eficiente y con menos código que las listas de Python nativas.

import numpy as np
# Crear un array unidimensional
array_unidimensional = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:", array_unidimensional)    
# Crear un array bidimensional (matriz)
array_bidimensional = np.array([[1, 2, 3], [4, 5, 6]])
print("Array bidimensional:\n", array_bidimensional)
# Crear un array tridimensional
array_tridimensional = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Array tridimensional:\n", array_tridimensional)
# Crear un array de ceros
array_ceros = np.zeros((3, 4))  # Array de 3 filas y 4 columnas lleno de ceros
print("Array de ceros:\n", array_ceros)




# Crear un array de NumPy
a = np.array([1, 2, 3, 4, 5])

# Realizar operaciones matemáticas
print("Suma de los elementos:", np.sum(a))
print("Media de los elementos:", np.mean(a))
print("Cuadrado de cada elemento:", a ** 2)