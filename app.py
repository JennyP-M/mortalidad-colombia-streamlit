import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import urllib.request

st.set_page_config(page_title="Mortalidad Colombia 2019", layout="wide")

st.title("Mortalidad en Colombia - Año 2019")
st.markdown("Aplicación desarrollada por **Jenny Marcela Patiño Aldana**")

# ==============================
# 1 CARGA DE DATOS
# ==============================
@st.cache_data
def cargar_datos():
    dat_no_fetal = pd.read_excel("Anexo1.NoFetal2019_CE_15-03-23.xlsx")
    CodigosDeMuerte = pd.read_excel("Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx")
    dat_depart = pd.read_excel("Divipola_CE_.xlsx")

    # Renombrar columnas
    CodigosDeMuerte = CodigosDeMuerte.rename(columns={
        'Código de la CIE-10 tres caracteres': 'COD_3_CARCT',
        'Descripción  de códigos mortalidad a tres caracteres': "DESCRIP_3_CARCT",
        'Código de la CIE-10 cuatro caracteres': 'COD_MUERTE',
        'Descripcion  de códigos mortalidad a cuatro caracteres': "DESCRIP_4_CARCT"
    })

    # Uniones
    dat_unido = pd.merge(dat_no_fetal, dat_depart, on=["COD_DANE", "COD_DEPARTAMENTO", "COD_MUNICIPIO"])
    dat_unido2 = pd.merge(dat_unido, CodigosDeMuerte, on=['COD_MUERTE'])
    return dat_unido2

DAT_UNIDO_2 = cargar_datos()

# ==============================
# 2 MENÚ DE VISUALIZACIONES
# ==============================
opcion = st.sidebar.selectbox(
    "Selecciona el gráfico a visualizar:",
    [
        "Mapa de muertes por departamento",
        "Muertes por mes",
        "Top 5 municipios con más homicidios (X95)",
        "10 municipios con menor mortalidad",
        "10 principales causas de muerte",
        "Comparación de muertes por sexo y departamento",
        "Distribución por grupo etario"
    ]
)

# ==============================
# 3 VISUALIZACIONES
# ==============================

if opcion == "Mapa de muertes por departamento":
    st.subheader("Distribución total de muertes por departamento (2019)")

    muertes_depto = DAT_UNIDO_2.groupby("DEPARTAMENTO").size().reset_index(name="Total_muertes")

    url = 'https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json'
    with urllib.request.urlopen(url) as response:
        colombia_geojson = json.loads(response.read().decode())

    nombre_mapping = {
        'ANTIOQUIA': 'ANTIOQUIA', 'ATLÁNTICO': 'ATLANTICO', 'BOGOTÁ, D.C.': 'SANTAFE DE BOGOTA D.C',
        'BOLÍVAR': 'BOLIVAR', 'BOYACÁ': 'BOYACA', 'CALDAS': 'CALDAS', 'CAQUETÁ': 'CAQUETA',
        'CAUCA': 'CAUCA', 'CESAR': 'CESAR', 'CÓRDOBA': 'CORDOBA', 'CUNDINAMARCA': 'CUNDINAMARCA',
        'CHOCÓ': 'CHOCO', 'HUILA': 'HUILA', 'LA GUAJIRA': 'LA GUAJIRA', 'MAGDALENA': 'MAGDALENA',
        'META': 'META', 'NARIÑO': 'NARIÑO', 'NORTE DE SANTANDER': 'NORTE DE SANTANDER', 'QUINDÍO': 'QUINDIO',
        'RISARALDA': 'RISARALDA', 'SANTANDER': 'SANTANDER', 'SUCRE': 'SUCRE', 'TOLIMA': 'TOLIMA',
        'VALLE DEL CAUCA': 'VALLE DEL CAUCA', 'ARAUCA': 'ARAUCA', 'CASANARE': 'CASANARE', 'PUTUMAYO': 'PUTUMAYO',
        'AMAZONAS': 'AMAZONAS', 'GUAINÍA': 'GUAINIA', 'GUAVIARE': 'GUAVIARE', 'VAUPÉS': 'VAUPES', 'VICHADA': 'VICHADA'
    }

    muertes_depto['depto_nombre'] = muertes_depto['DEPARTAMENTO'].map(nombre_mapping)

    fig = go.Figure(go.Choroplethmapbox(
        geojson=colombia_geojson,
        locations=muertes_depto['depto_nombre'],
        z=muertes_depto['Total_muertes'],
        featureidkey="properties.NOMBRE_DPT",
        colorscale='Reds',
        colorbar=dict(title="Total Muertes"),
        text=muertes_depto['DEPARTAMENTO'],
        hovertemplate='<b>%{text}</b><br>Muertes: %{z:,.0f}<extra></extra>'
    ))

    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=4.5,
        mapbox_center={"lat": 4.5, "lon": -74},
        height=700
    )

    st.plotly_chart(fig, use_container_width=True)

elif opcion == "Muertes por mes":
    muertes_mes = DAT_UNIDO_2.groupby("MES").size().reset_index(name="TOTAL_MUERTES")
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
        7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    muertes_mes["MES_NOMBRE"] = muertes_mes["MES"].map(meses)

    fig = px.line(muertes_mes, x="MES_NOMBRE", y="TOTAL_MUERTES", markers=True,
                  title="Total de muertes por mes - 2019")
    st.plotly_chart(fig, use_container_width=True)

elif opcion == "Top 5 municipios con más homicidios (X95)":
    df_homicidios = DAT_UNIDO_2[DAT_UNIDO_2["COD_3_CARCT"] == "X95"]
    top_municipios = (df_homicidios.groupby('MUNICIPIO')
                      .size().reset_index(name='Total_homicidios')
                      .sort_values(by='Total_homicidios', ascending=False).head(5))
    fig = px.bar(top_municipios, x='Total_homicidios', y='MUNICIPIO', orientation='h',
                 title='Top 5 municipios con más homicidios (X95)')
    st.plotly_chart(fig, use_container_width=True)

elif opcion == "10 municipios con menor mortalidad":
    muertes_por_mpio = (DAT_UNIDO_2.groupby('MUNICIPIO')
                        .size().reset_index(name='Total_muertes')
                        .sort_values(by='Total_muertes', ascending=True).head(10))
    fig = px.pie(muertes_por_mpio, names='MUNICIPIO', values='Total_muertes',
                 title='10 municipios con menor mortalidad')
    st.plotly_chart(fig, use_container_width=True)

elif opcion == "10 principales causas de muerte":
    top_causas = (DAT_UNIDO_2.groupby(['MANERA_MUERTE', 'COD_3_CARCT'])
                  .size().reset_index(name='Total_casos')
                  .sort_values(by='Total_casos', ascending=False).head(10))
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Manera de muerte', 'Código', 'Total casos'], fill_color='darkblue', font=dict(color='white')),
        cells=dict(values=[top_causas[k] for k in ['MANERA_MUERTE', 'COD_3_CARCT', 'Total_casos']])
    )])
    st.plotly_chart(fig, use_container_width=True)

elif opcion == "Comparación de muertes por sexo y departamento":
    muertes_sexo_depto = (DAT_UNIDO_2.groupby(['DEPARTAMENTO', 'SEXO'])
                          .size().reset_index(name='Total_muertes'))
    muertes_sexo_depto['SEXO'] = muertes_sexo_depto['SEXO'].replace({1: 'Masculino', 2: 'Femenino', 3: 'Indeterminado'})
    fig = px.bar(muertes_sexo_depto, x='DEPARTAMENTO', y='Total_muertes', color='SEXO',
                 title='Muertes por sexo y departamento')
    st.plotly_chart(fig, use_container_width=True)

elif opcion == "Distribución por grupo etario":
    df = DAT_UNIDO_2.copy()
    bins = [-1, 4, 6, 8, 10, 11, 13, 16, 19, 24, 28, 29]
    labels = [
        "Neonatal (<1 mes)", "Infantil (1-11 meses)", "Primera infancia (1-4 años)",
        "Niñez (5-14)", "Adolescencia (15-19)", "Juventud (20-29)", "Adultez temprana (30-44)",
        "Adultez intermedia (45-59)", "Vejez (60-84)", "Longevidad (85+)", "Desconocida"
    ]
    df["GRUPO_EDAD_CAT"] = pd.cut(df["GRUPO_EDAD1"], bins=bins, labels=labels, include_lowest=True)
    dist_edad = df["GRUPO_EDAD_CAT"].value_counts().reset_index()
    dist_edad.columns = ["Grupo de edad", "Total_muertes"]
    fig = px.bar(dist_edad, x="Grupo de edad", y="Total_muertes", text="Total_muertes",
                 title="Distribución de muertes por grupo etario (2019)")
    st.plotly_chart(fig, use_container_width=True)
