import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Solicitudes",
    page_icon="📊",
    layout="wide"
)

# Sidebar personalizado
st.sidebar.title("Menú Principal")
st.sidebar.write("Selecciona una opción para continuar:")

# Opciones en el sidebar
opcion = st.sidebar.selectbox(
    "Opciones:",
    ["Inicio", "Solicites", "Solicitudes Vigentes"]
)

# Contenido principal según la opción seleccionada
if opcion == "Inicio":
    st.title("Bienvenido al Dashboard")
    st.write("Explora los datos y gráficos disponibles.")
elif opcion == "Solicites":
    # URL de tu servicio en Django
    SERVICE_URL = "http://186.113.21.35:8060/informes/vwsolicitudes/"

    # Consumir datos del servicio
    response = requests.get(SERVICE_URL)
    if response.status_code == 200:
        data = response.json()
    else:
        st.error("Error al obtener los datos.")
        st.stop()

    # Convertir datos a DataFrame
    df = pd.DataFrame(data)
    st.dataframe(df)  # Mostrar tabla en Streamlit


    # Crear gráfico de barras con Matplotlib
    fig, ax = plt.subplots()
    ax.bar(df['depto_nombre'], df['nosolicitud'], color='skyblue')
    ax.set_xlabel('Departamento')
    ax.set_ylabel('Número de Solicitudes')
    ax.set_title('Solicitudes por Departamento')
    plt.xticks(rotation=45)
    st.pyplot(fig)
elif opcion == "Solicitudes Vigentes":
    st.title("Informe de Solicitudes Vigentes")
    
    SERVICE_URL = "http://186.113.21.35:8060/informes/solicitudes-vigentes/"
    
    response = requests.get(SERVICE_URL)
    if response.status_code == 200:
        data = response.json()
    else:
        st.error("Error al obtener los datos.")
        st.stop()
        
    # Convertir datos a DataFrame
    df = pd.DataFrame(data)
    
    # Mostrar las métricas como recuadros
    st.markdown("## Métricas principales")
    
    # Crear un contenedor horizontal
    col1, col2, col3, col4 = st.columns(4)

    # Métrica: Total de Solicitudes
    col1.metric(label="Total de Solicitudes", value=df['NoSolicitud'].nunique())

    # Métrica: Total de Clientes
    col2.metric(label="Total de Clientes", value=df['ClienteIdentificacion'].nunique())

    # Métrica: Media Vr Credito
    media_vr_credito = f"${df['vr_credito'].mean():,.0f}"
    col3.metric(label="Media Vr Credito", value=media_vr_credito)

    # Métrica: Media Vr Proyecto
    media_vr_proyecto = f"${df['vr_proyecto'].mean():,.0f}"
    col4.metric(label="Media Vr Proyecto", value=media_vr_proyecto)

    # Agrupar los datos por TipoProductor y contar las solicitudes
    tipo_productor_data = df['TipoProductor'].value_counts().reset_index()
    tipo_productor_data.columns = ['TipoProductor', 'Count']

    # Crear el gráfico de torta
    fig = px.pie(
        tipo_productor_data,
        names='TipoProductor',
        values='Count',
        title='Distribución de Solicitudes por Tipo de Productor',
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    # Agrupar los datos por ActividadEconomica y contar valores únicos de NoSolicitud
    actividad_data = df.groupby('ActividadEconomica')['NoSolicitud'].nunique().reset_index()
    actividad_data.columns = ['ActividadEconomica', 'Count']  # Renombrar columnas

    # Crear el gráfico de barras
    fig = px.bar(
        actividad_data,
        x='ActividadEconomica',
        y='Count',
        title='Cantidad de Solicitudes por Actividad Económica',
        labels={'ActividadEconomica': 'Actividad Económica', 'Count': 'Cantidad de Solicitudes'},
        color='Count',  # Colorear según la cantidad
        color_continuous_scale=px.colors.sequential.Viridis
    )

    # Personalizar diseño del gráfico
    fig.update_layout(
        xaxis_tickangle=-45,  # Rotar etiquetas en el eje X
        xaxis_title="Actividad Económica",
        yaxis_title="Cantidad de Solicitudes"
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)
elif opcion == "Acerca de":
    st.title("Acerca de")
    st.write("Información sobre la aplicación.")
