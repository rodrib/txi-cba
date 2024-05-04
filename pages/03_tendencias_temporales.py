import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
file_path = "taxi-all-23-3.csv"  # Reemplaza con la ubicación de tu archivo CSV
df = pd.read_csv(file_path)

# Convertir la columna 'Fecha' a formato datetime
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m')

# Limpiar la columna 'saldo' y luego convertir a flotante
df['saldo'] = df['saldo'].str.replace(',', '').str.replace('.', '').astype(float)

# Ordenar los datos por fecha
df = df.sort_values('Fecha')

# Agrupar los datos por mes y calcular el saldo promedio
monthly_balance = df.groupby(df['Fecha'].dt.to_period('M'))['saldo'].mean()

# Configurar la interfaz de Streamlit
st.title('Visualización de Saldo Promedio Mensual')
st.write('Saldo promedio por mes a lo largo del tiempo')

# Visualizar el saldo promedio por mes
plt.figure(figsize=(10, 6))
monthly_balance.plot(kind='line', marker='o', color='b')
plt.title('Saldo Promedio Mensual')
plt.xlabel('Fecha')
plt.ylabel('Saldo Promedio')
plt.grid(True)

# Mostrar la visualización en Streamlit
st.pyplot(plt)
