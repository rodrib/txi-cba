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


# Ahora, realiza el análisis de datos financieros usando el CSV ya cargado
# Definir las funciones de análisis de datos
def cuentas_unicas(datos):
    return datos['cuenta'].nunique()





def cuenta_con_mayor_credito(datos):
    return datos.loc[datos['credito'].idxmax()]['cuenta']

def cuentas_mas_repetidas(datos, n=5):
    cuentas_repetidas = datos['cuenta'].value_counts().head(n)
    cuentas_destinatario = {}
    for cuenta in cuentas_repetidas.index:
        destinatario = datos[datos['cuenta'] == cuenta]['destinatario'].iloc[0]
        cuentas_destinatario[cuenta] = destinatario
    return cuentas_destinatario


st.title("Análisis de datos financieros")

# Botón para ejecutar el análisis
if st.button("Realizar análisis"):
    st.write("Número de cuentas únicas:", cuentas_unicas(df))
    #st.write("Cuenta con mayor débito:", cuenta_con_mayor_debito(df))
    #st.write("Cuenta con mayor crédito:", cuenta_con_mayor_credito(df))
    st.write("5 primeras cuentas más repetidas:")
    cuentas_repetidas = cuentas_mas_repetidas(df)
    for cuenta, destinatario in cuentas_repetidas.items():
        st.write(f"Cuenta: {cuenta}, Destinatario: {destinatario}")