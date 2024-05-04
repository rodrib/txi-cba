import streamlit as st
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("taxi-all-23-3.csv")

# Mostrar el DataFrame en Streamlit
st.title("Taxi-Cordoba")
#st.dataframe(df)

# Función para mostrar todos los valores de "SALDO RES. ANTERIOR"
def mostrar_saldos_anteriores():
    # Filtrar las filas que contienen "SALDO RES. ANTERIOR" en la columna "Concepto"
    saldos_anteriores = df[df['Concepto'] == 'SALDO RES. ANTERIOR']
    
    # Mostrar los valores en una tabla
    if not saldos_anteriores.empty:
        st.write("Valores de 'SALDO RES. ANTERIOR':")
        st.write(saldos_anteriores[['Concepto', 'saldo', 'Asiento']])
    else:
        st.write("No se encontraron valores de 'SALDO RES. ANTERIOR'")

# Botón para mostrar todos los valores de "SALDO RES. ANTERIOR"
if st.button("Mostrar todos los valores de SALDO RES. ANTERIOR"):
    mostrar_saldos_anteriores()


# Datos
saldos = [
    625463.43,
    623166.54,
    691768.11,
    810544.51,
    384035.94,
    354512.78,
    194530.95,
    972569.29,
    1295412.71,
    894850.89,
    1521975.84
]

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre"
]

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(meses, saldos, color='skyblue')
ax.set_xlabel('Mes')
ax.set_ylabel('Saldo')
ax.set_title('Saldo por Mes')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


# Limpiar y convertir la columna de saldo a flotante
df['saldo'] = df['saldo'].str.replace('.', '').str.replace(',', '.').astype(float)

# Crear el gráfico de distribución
fig, ax = plt.subplots()
ax.hist(df['saldo'], bins=30, color='skyblue', edgecolor='black')
ax.set_title('Distribución del Saldo')
ax.set_xlabel('Saldo')
ax.set_ylabel('Frecuencia')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)