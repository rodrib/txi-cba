import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer

# Cargar los datos
file_path = "taxi-all-23-3.csv"  # Reemplaza con la ubicación de tu archivo CSV
df = pd.read_csv(file_path)

# Limpiar y convertir las columnas relevantes a flotantes
df['debito'] = df['debito'].str.replace('.', '').str.replace(',', '.').astype(float)
df['credito'] = df['credito'].str.replace('.', '').str.replace(',', '.').astype(float)
df['saldo'] = df['saldo'].str.replace('.', '').str.replace(',', '.').astype(float)

# Imputar valores faltantes con ceros
imputer = SimpleImputer(strategy='constant', fill_value=0)
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Seleccionar características relevantes
features = ['debito', 'credito', 'saldo']

# Crear y entrenar el modelo Isolation Forest
model = IsolationForest(contamination=0.05)  # Establecer el porcentaje de valores atípicos esperados
model.fit(df_imputed[features])

# Predecir valores atípicos
outliers = model.predict(df_imputed[features])

# Agregar la columna de valores atípicos al DataFrame original
df_imputed['outlier'] = outliers

# Filtrar solo las transacciones consideradas como valores atípicos
outlier_transactions = df_imputed[df_imputed['outlier'] == -1]

# Visualizar los resultados
st.write("Transacciones consideradas como valores atípicos:")
st.write(outlier_transactions)
