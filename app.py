import streamlit as st
from multipage import MultiPage
from pages import home, graficos, formulario  # Importa tus páginas

<<<<<<< HEAD
# Configura el título de la aplicación
st.set_page_config(page_title="Mi App", layout="wide")
=======
# URL de tu servicio en Django
SERVICE_URL = "http://186.113.21.35:8060/informes/vwsolicitudes/"
>>>>>>> 63ceda31241e69e2952b3bfcf29a7b2c1743d24c

# Crea la instancia de navegación
app = MultiPage()

# Agrega las páginas con un título y la función asociada
app.add_page("Inicio", home.app)
app.add_page("Gráficos", graficos.app)
app.add_page("Formulario", formulario.app)

# Corre la app
app.run()

# import streamlit as st
# import requests
# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px

# # URL de tu servicio en Django
# SERVICE_URL = "http://127.0.0.1:8000/informes/vwsolicitudes/"

# # Consumir datos del servicio
# response = requests.get(SERVICE_URL)
# if response.status_code == 200:
#     data = response.json()
# else:
#     st.error("Error al obtener los datos.")
#     st.stop()

# # Convertir datos a DataFrame
# df = pd.DataFrame(data)
# st.dataframe(df)  # Mostrar tabla en Streamlit


# # Crear gráfico de barras con Matplotlib
# fig, ax = plt.subplots()
# ax.bar(df['depto_nombre'], df['nosolicitud'], color='skyblue')
# ax.set_xlabel('Departamento')
# ax.set_ylabel('Número de Solicitudes')
# ax.set_title('Solicitudes por Departamento')
# plt.xticks(rotation=45)
# st.pyplot(fig)

<<<<<<< HEAD
# # Crear gráfico interactivo con Plotly
# fig = px.bar(df, x='depto_nombre', y='nosolicitud', 
#              title='Solicitudes por Departamento', 
#              labels={'depto_nombre': 'Departamento', 'nosolicitud': 'Número de Solicitudes'})
# st.plotly_chart(fig)
=======
# Crear gráfico interactivo con Plotly
fig = px.bar(df, x='depto_nombre', y='nosolicitud', 
             title='Solicitudes por Departamento', 
             labels={'depto_nombre': 'Departamento', 'nosolicitud': 'Número de Solicitudes'})
st.plotly_chart(fig)
>>>>>>> 63ceda31241e69e2952b3bfcf29a7b2c1743d24c
