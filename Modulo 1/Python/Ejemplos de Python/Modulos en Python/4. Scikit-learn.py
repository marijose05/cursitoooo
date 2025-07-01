# Scikit-learn es una de las librerías de aprendizaje automático (machine learning) más 
# populares y accesibles. Proporciona herramientas simples y eficientes para el análisis 
# predictivo de datos. Incluye una vasta gama de algoritmos para tareas de clasificación, 
# regresión, clustering y reducción de dimensionalidad, junto con utilidades para la evaluación 
# y selección de modelos.

from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de ejemplo (características y etiquetas)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Predecir un nuevo valor
new_X = np.array([[6]])
prediction = model.predict(new_X)

print(f"La predicción para el valor 6 es: {prediction[0]}")

