import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

def main():
    st.title("Predicción del Saldo Futuro")

    # Cargar el archivo CSV
    file_path = "taxi-all-23-3.csv"  # Reemplaza "ruta/a/tu/archivo.csv" con la ubicación de tu archivo CSV
    df = pd.read_csv(file_path)

    # Eliminar comas y puntos de la columna 'debito' y luego convertir a flotante
    df['debito'] = df['debito'].str.replace(',', '').str.replace('.', '').astype(float)

    # Limpiar la columna 'saldo' y luego convertir a flotante
    df['saldo'] = df['saldo'].str.replace(',', '').str.replace('.', '').astype(float)

    # Mostrar los primeros registros del DataFrame
    st.subheader("Primeros registros del DataFrame:")
    st.write(df.head())

    # Manejar los valores faltantes
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(imputer.fit_transform(df[['debito', 'saldo']]), columns=['debito', 'saldo'])
    
    # Separar variables predictoras (X) y variable objetivo (y)
    X = df_imputed[['debito']]  # Variable predictora: débito
    y = df_imputed['saldo']  # Variable objetivo: saldo

    # Entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X, y)

    # Mostrar los coeficientes del modelo
    st.subheader("Coeficientes del modelo:")
    st.write(model.coef_)

if __name__ == "__main__":
    main()



