import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('taxi-all-23-2.csv')

# Convertir la columna de fecha a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m')

# Eliminar las filas con saldo nulo
df = df.dropna(subset=['saldo'])

# Crear una variable de tiempo
df['Tiempo'] = (df['Fecha'] - df['Fecha'].min()).dt.days

# Dividir los datos en características (X) y la variable objetivo (y)
X = df[['Tiempo']]
y = df['saldo']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE: {mse}')
print(f'R^2: {r2}')

# Visualizar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.title('Predicción de Saldo Futuro')
plt.xlabel('Tiempo (días)')
plt.ylabel('Saldo')
plt.grid(True)
plt.show()
