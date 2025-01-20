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
    # st.dataframe(df)  # Mostrar tabla en Streamlit

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
    
    # Filtros disponibles
    departamentos = df["depto_nombre"].unique()
    municipios = df["ciudad_nombre"].unique()
    tipos_productor = df["TipoProductor"].unique()
    actividades_economicas = df["ActividadEconomica"].unique()

    # Inicializar filtros en st.session_state si no están ya
    if 'departamentos_seleccionados' not in st.session_state:
        st.session_state.departamentos_seleccionados = []
    if 'municipios_seleccionados' not in st.session_state:
        st.session_state.municipios_seleccionados = []
    if 'tipos_productor_seleccionados' not in st.session_state:
        st.session_state.tipos_productor_seleccionados = []
    if 'actividades_seleccionadas' not in st.session_state:
        st.session_state.actividades_seleccionadas = []

    # Filtros de selección múltiple
    departamentos_seleccionados = st.multiselect(
        "Selecciona los departamentos:",
        options=departamentos,
        default=st.session_state.departamentos_seleccionados
    )

    municipios_seleccionados = st.multiselect(
        "Selecciona los municipios:",
        options=municipios,
        default=st.session_state.municipios_seleccionados
    )

    tipos_productor_seleccionados = st.multiselect(
        "Selecciona los tipos de productor:",
        options=tipos_productor,
        default=st.session_state.tipos_productor_seleccionados
    )

    actividades_seleccionadas = st.multiselect(
        "Selecciona las actividades económicas:",
        options=actividades_economicas,
        default=st.session_state.actividades_seleccionadas
    )

    # Guardar los filtros seleccionados en session_state
    st.session_state.departamentos_seleccionados = departamentos_seleccionados
    st.session_state.municipios_seleccionados = municipios_seleccionados
    st.session_state.tipos_productor_seleccionados = tipos_productor_seleccionados
    st.session_state.actividades_seleccionadas = actividades_seleccionadas

    # Verificar si se seleccionaron filtros
    if not departamentos_seleccionados and not municipios_seleccionados and not tipos_productor_seleccionados and not actividades_seleccionadas:
        st.warning("Por favor, selecciona al menos una opción en cada filtro.")
    else:
        # Filtrar el DataFrame con los filtros seleccionados
        df_filtrado = df[
            df["depto_nombre"].isin(departamentos_seleccionados) &
            df["ciudad_nombre"].isin(municipios_seleccionados) &
            df["TipoProductor"].isin(tipos_productor_seleccionados) &
            df["ActividadEconomica"].isin(actividades_seleccionadas)
        ]

        # Crear un contenedor horizontal
        col1, col2, col3, col4 = st.columns(4)

        # Métrica: Total de Solicitudes
        col1.metric(label="Total de Solicitudes", value=df_filtrado['NoSolicitud'].nunique())

        # Métrica: Total de Clientes
        col2.metric(label="Total de Clientes", value=df_filtrado['ClienteIdentificacion'].nunique())

        # Métrica: Media Vr Credito
        media_vr_credito = f"${df_filtrado['vr_credito'].mean():,.0f}"
        col3.metric(label="Media Vr Credito", value=media_vr_credito)

        # Métrica: Media Vr Proyecto
        media_vr_proyecto = f"${df_filtrado['vr_proyecto'].mean():,.0f}"
        col4.metric(label="Media Vr Proyecto", value=media_vr_proyecto)
        
        col1, col2 = st.columns(2)
        
        media_vr_proyecto = f"${df_filtrado['vr_credito'].sum():,.0f}"
        col1.metric(label="Vr Total Credito", value=media_vr_proyecto)
        
        media_vr_proyecto = f"${df_filtrado['vr_proyecto'].sum():,.0f}"
        col2.metric(label="Vr Total Proyecto", value=media_vr_proyecto)

        # Crear contenedores en columnas para mostrar los gráficos lado a lado
        col1, col2 = st.columns(2)

        # Gráfico de torta: Distribución por Tipo de Productor (en la primera columna)
        with col1:
            st.subheader("Distribución por Tipo de Productor")
            fig_torta = px.pie(
                df_filtrado,
                names="TipoProductor",
                title="Distribución por Tipo de Productor",
                values="NoSolicitud",
                color_discrete_sequence=px.colors.sequential.RdBu,
            )
            st.plotly_chart(fig_torta, use_container_width=True)

        # Gráfico de barras: Solicitudes por Actividad Económica (en la segunda columna)
        with col2:
            st.subheader("Solicitudes por Actividad Económica")
            
            # Agrupar, contar y ordenar
            actividad_data = (
                df_filtrado.groupby("ActividadEconomica")["NoSolicitud"]
                .count()
                .reset_index()
                .sort_values(by="NoSolicitud", ascending=False)  # Ordenar de mayor a menor
                .head(15)  # Tomar solo las primeras 15 filas
            )
            
            # Crear el gráfico de barras
            fig_barras = px.bar(
                actividad_data,
                x="ActividadEconomica",
                y="NoSolicitud",
                color="ActividadEconomica",
                title="Top 15: Número de Solicitudes por Actividad Económica",
                labels={"NoSolicitud": "Cantidad de Solicitudes"},
            )
            
            # Mostrar el gráfico
            st.plotly_chart(fig_barras, use_container_width=True)

        st.subheader("Rubros")
            
        # Agrupar, contar y ordenar
        actividad_data = (
            df_filtrado.groupby("rubro_nombre")["NoSolicitud"]
            .count()
            .reset_index()
            .sort_values(by="NoSolicitud", ascending=False)  # Ordenar de mayor a menor
            .head(15)  # Tomar solo las primeras 15 filas
        )
        
        # Crear el gráfico de barras
        fig_barras = px.bar(
            actividad_data,
            x="rubro_nombre",
            y="NoSolicitud",
            color="rubro_nombre",
            # title="Top 15: Número de Solicitudes por Actividad Económica",
            labels={"NoSolicitud": "Cantidad de Solicitudes"},
        )
        
        # Mostrar el gráfico
        st.plotly_chart(fig_barras, use_container_width=True)

        # Tabla dinámica
        st.subheader("Detalle de Solicitudes")
        st.dataframe(df_filtrado)

        # Gráfico temporal: Solicitudes por fecha
        st.subheader("Tendencia Temporal de Solicitudes")
        temporal_data = df_filtrado.groupby("FechaRadicacion")["NoSolicitud"].count().reset_index()
        fig_lineas = px.line(
            temporal_data,
            x="FechaRadicacion",
            y="NoSolicitud",
            title="Tendencia de Solicitudes en el Tiempo",
            labels={"FechaRadicacion": "Fecha", "NoSolicitud": "Cantidad de Solicitudes"},
        )
        st.plotly_chart(fig_lineas, use_container_width=True)
elif opcion == "Acerca de":
    st.title("Acerca de")
    st.write("Información sobre la aplicación.")

