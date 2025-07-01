# Matplotlib es la librería de visualización de datos por excelencia en Python. 
# Permite crear una amplia variedad de gráficos estáticos, animados e interactivos 
# de alta calidad. Es altamente personalizable, lo que brinda un control total sobre 
# cada aspecto de una figura.

import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear un gráfico de líneas
plt.plot(x, y, marker='o')

# Añadir títulos y etiquetas
plt.title("Gráfico de Líneas Simple")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar el gráfico
plt.show()

# Crear un gráfico de barras
plt.bar(x, y, color='skyblue')  
# Añadir títulos y etiquetas
plt.title("Gráfico de Barras Simple")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
# Mostrar el gráfico
plt.show()
# Crear un gráfico de dispersión
plt.scatter(x, y, color='red', marker='x')
# Añadir títulos y etiquetas
plt.title("Gráfico de Dispersión Simple")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
# Mostrar el gráfico
plt.show()
