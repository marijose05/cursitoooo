# Construido sobre NumPy, Pandas es una librería esencial para la manipulación y el análisis de datos. 
# Introduce dos estructuras de datos principales: la Serie (unidimensional) y el DataFrame (bidimensional), 
# que se asemejan a una columna y a una tabla de una hoja de cálculo o una base de datos SQL, respectivamente. 
# Pandas facilita enormemente tareas como la lectura y escritura de datos, la limpieza, la transformación y el análisis exploratorio.

import pandas as pd

# Crear un DataFrame
data = {'Nombre': ['Ana', 'Luis', 'Carlos'],
        'Edad': [28, 34, 29],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Filtrar datos
print("\nPersonas mayores de 30 años:")
print(df[df['Edad'] > 30])

# Agrupar datos
print("\nMedia de edad por ciudad:")    
print(df.groupby('Ciudad')['Edad'].mean())
# Ordenar datos
print("\nDatos ordenados por edad:")
print(df.sort_values(by='Edad'))
# Añadir una nueva columna
df['Salario'] = [30000, 45000, 40000]
print("\nDataFrame con nueva columna 'Salario':")
print(df)   