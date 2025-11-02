
##############
####### ACTIVIDAD 4 : APLICACIONES l #####
##### Jenny Marcela Patiño Aldana

### cargamos los paquetes necesarios
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
import requests
import urllib.request
### Cargamos los archivos
dat_no_fetal=pd.read_excel(r"C:\Users\jenny.patino\OneDrive - 35159_147728_DUPREE_VENTA_DIRECTA_S_A\Documentos\ACTV 4\Anexo1.NoFetal2019_CE_15-03-23.xlsx")
dat_no_fetal.head()

CodigosDeMuerte=pd.read_excel(r"C:\Users\jenny.patino\OneDrive - 35159_147728_DUPREE_VENTA_DIRECTA_S_A\Documentos\ACTV 4\Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx")
CodigosDeMuerte.head()

dat_depart=pd.read_excel(r"C:\Users\jenny.patino\OneDrive - 35159_147728_DUPREE_VENTA_DIRECTA_S_A\Documentos\ACTV 4\Divipola_CE_.xlsx")
dat_depart.head()

#HACEMOS LA UNION DE DATOS
#UNIMOS dat_no_fetal CON dat_depart POR LA LLAVE COD DANE, COD_DEPARTAMENTO Y COD_MUNICIPIO
dat_no_fetal.info()
dat_depart.info()

DAT_UNIDO=pd.merge(dat_no_fetal, dat_depart, on=["COD_DANE", "COD_DEPARTAMENTO", "COD_MUNICIPIO"])
len(dat_no_fetal)
len(dat_depart)
len(DAT_UNIDO)
DAT_UNIDO.head()

#hacemos la segunda unión
CodigosDeMuerte.columns
CodigosDeMuerte= CodigosDeMuerte.rename(columns={'Código de la CIE-10 tres caracteres': 'COD_3_CARCT',
                                                 'Descripción  de códigos mortalidad a tres caracteres': "DESCRIP_3_CARCT",
                                                 'Código de la CIE-10 cuatro caracteres': 'COD_MUERTE',
                                                  'Descripcion  de códigos mortalidad a cuatro caracteres': "DESCRIP_4_CARCT"})


DAT_UNIDO_2=pd.merge(DAT_UNIDO, CodigosDeMuerte, on=['COD_MUERTE'])
len(CodigosDeMuerte)
len(DAT_UNIDO)
len(DAT_UNIDO_2)
DAT_UNIDO_2.info()
DAT_UNIDO_2.head()
DAT_UNIDO_2.AÑO.unique()
DAT_UNIDO_2.columns

#####################
##### gráfico 1: Mapa de Colombia

# Contar número de registros (muertes) por departamento
muertes_depto = DAT_UNIDO_2.groupby("DEPARTAMENTO").size().reset_index(name="Total_muertes")
muertes_depto.columns 
# Revisar el resultado
print(muertes_depto.head())

print(muertes_depto.head(10))
print("\n")
print(muertes_depto['DEPARTAMENTO'].unique())



# Cargar GeoJSON de Colombia desde una fuente pública
url = 'https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json'

with urllib.request.urlopen(url) as response:
    colombia_geojson = json.loads(response.read().decode())

# Suponiendo que ya tienes tu DataFrame cargado
# muertes_depto = pd.read_csv('tu_archivo.csv')

# Normalizar nombres de departamentos para que coincidan con el GeoJSON
# El GeoJSON usa nombres en MAYÚSCULAS SIN TILDES
nombre_mapping = {
    'ANTIOQUIA': 'ANTIOQUIA',
    'ATLÁNTICO': 'ATLANTICO',
    'BOGOTÁ, D.C.': 'SANTAFE DE BOGOTA D.C',
    'BOLÍVAR': 'BOLIVAR',
    'BOYACÁ': 'BOYACA',
    'CALDAS': 'CALDAS',
    'CAQUETÁ': 'CAQUETA',
    'CAUCA': 'CAUCA',
    'CESAR': 'CESAR',
    'CÓRDOBA': 'CORDOBA',
    'CUNDINAMARCA': 'CUNDINAMARCA',
    'CHOCÓ': 'CHOCO',
    'HUILA': 'HUILA',
    'LA GUAJIRA': 'LA GUAJIRA',
    'MAGDALENA': 'MAGDALENA',
    'META': 'META',
    'NARIÑO': 'NARIÑO',
    'NORTE DE SANTANDER': 'NORTE DE SANTANDER',
    'QUINDÍO': 'QUINDIO',
    'RISARALDA': 'RISARALDA',
    'SANTANDER': 'SANTANDER',
    'SUCRE': 'SUCRE',
    'TOLIMA': 'TOLIMA',
    'VALLE DEL CAUCA': 'VALLE DEL CAUCA',
    'ARAUCA': 'ARAUCA',
    'CASANARE': 'CASANARE',
    'PUTUMAYO': 'PUTUMAYO',
    'AMAZONAS': 'AMAZONAS',
    'GUAINÍA': 'GUAINIA',
    'GUAVIARE': 'GUAVIARE',
    'VAUPÉS': 'VAUPES',
    'VICHADA': 'VICHADA'
}

# Agregar columna con nombres normalizados
muertes_depto['depto_nombre'] = muertes_depto['DEPARTAMENTO'].map(nombre_mapping)

# Crear el mapa coroplético
fig = go.Figure(go.Choroplethmapbox(
    geojson=colombia_geojson,
    locations=muertes_depto['depto_nombre'],
    z=muertes_depto['Total_muertes'],
    featureidkey="properties.NOMBRE_DPT",  # Clave en el GeoJSON
    colorscale='Reds',
    colorbar=dict(title="Total Muertes"),
    text=muertes_depto['DEPARTAMENTO'],
    hovertemplate='<b>%{text}</b><br>Muertes: %{z:,.0f}<extra></extra>',
    marker_line_width=1,
    marker_line_color='white'
))

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=4.5,
    mapbox_center={"lat": 4.5, "lon": -74},
    title_text='Distribución Total de Muertes por Departamento en Colombia - 2019',
    title_x=0.5,
    height=700,
    width=900,
    margin={"r":0,"t":50,"l":0,"b":0}
)

fig.show()

########################
#### GRAFICO 2: LINEAL POR MES ####
# Agrupar por mes
muertes_mes = DAT_UNIDO_2.groupby("MES").size().reset_index(name="TOTAL_MUERTES")

# Ordenar los meses si es necesario
muertes_mes = muertes_mes.sort_values("MES")
fig = px.line(
    muertes_mes,
    x="MES",
    y="TOTAL_MUERTES",
    markers=True,  # agrega puntos en la línea
    title="Total de muertes por mes en Colombia - 2019",
    labels={
        "MES": "Mes",
        "TOTAL_MUERTES": "Número de muertes"
    }
)

fig.update_layout(
    xaxis=dict(tickmode="linear", dtick=1),
    plot_bgcolor="white",
    title_x=0.5,
    title_font=dict(size=20)
)

fig.show()
# Diccionario de meses
meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

muertes_mes["MES_NOMBRE"] = muertes_mes["MES"].map(meses)

fig = px.line(
    muertes_mes,
    x="MES_NOMBRE",
    y="TOTAL_MUERTES",
    markers=True,
    title="Total de muertes por mes en Colombia - 2019"
)
fig.update_layout(title_x=0.5)
fig.show()

#######################
### GRAFICO 3: 
# Filtrar solo homicidios por arma de fuego (X95)
df_homicidios = DAT_UNIDO_2[DAT_UNIDO_2["COD_3_CARCT"] == "X95"]
# Contar homicidios por municipio
homicidios_municipio = (
    df_homicidios["MUNICIPIO"]
    .value_counts()
    .reset_index()
    .rename(columns={"index": "MUNICIPIO", "MUNICIPIO": "TOTAL_HOMICIDIOS"})
)

# Quedarse con los 5 primeros
top5_municipios = homicidios_municipio.head(5)
top5_municipios.columns
top5_municipios["MUNICIPIO"] = top5_municipios["count"]

#### grafico
# Filtrar homicidios (Cód. X95)
df_homicidios = DAT_UNIDO_2[DAT_UNIDO_2['COD_3_CARCT'] == 'X95']

# Agrupar por municipio y contar casos
top_municipios = (
    df_homicidios.groupby('MUNICIPIO')
    .size()
    .reset_index(name='Total_homicidios')
    .sort_values(by='Total_homicidios', ascending=False)
    .head(5)
)

# Crear gráfico de barras horizontal
# Crear gráfico de barras horizontal
fig2 = px.bar(
    top_municipios,
    x='Total_homicidios',
    y='MUNICIPIO',
    orientation='h',
    color='Total_homicidios',
    color_continuous_scale='plasma',
    title='Top 5 municipios con más homicidios (Cód. X95)<br>Colombia, año 2019'
)

# Ajustes estéticos y de layout
fig2.update_layout(
    title={
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 16},   # 🔹 tamaño de letra reducido
        'y': 0.97
    },
    xaxis_title='Número de homicidios',
    yaxis_title='Municipio',
    coloraxis_showscale=False,
    plot_bgcolor='white',
    height=600,
    margin=dict(l=180, r=80, t=120, b=50)
)

# Ajustar etiquetas y tooltip
fig2.update_traces(
    text=None,
    hovertemplate='<b>%{y}</b><br>Homicidios: %{x}<extra></extra>'
)

fig2.show()

###########################
#### grafico 4: circular ####
##################

# Contar número de defunciones por municipio
muertes_por_mpio = (
    DAT_UNIDO_2.groupby('MUNICIPIO')
    .size()
    .reset_index(name='Total_muertes')
    .sort_values(by='Total_muertes', ascending=True)
    .head(10)
)

# Crear gráfico circular
fig3 = px.pie(
    muertes_por_mpio,
    names='MUNICIPIO',
    values='Total_muertes',
    title='10 municipios con menor índice de mortalidad<br>Colombia, año 2019',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# Ajustar detalles del gráfico
fig3.update_traces(
    textinfo='percent+label',   # Mostrar porcentaje + nombre
    pull=[0.05]*10,             # Separar ligeramente todas las porciones
    textfont_size=12
)

# Ajustes del diseño
fig3.update_layout(
    title={
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 16},   # 🔹 tamaño de letra más pequeño
        'y': 0.97
    },
    legend=dict(
        orientation='h',       # Leyenda horizontal
        yanchor='top',
        y=-0.1,                # 🔹 La mueve debajo del gráfico
        xanchor='center',
        x=0.5
    ),
    height=600,
    plot_bgcolor='white',
    margin=dict(t=100, b=100)
)

fig3.show()

############################
##### gráfico 5: Tabla ####
##############################

# Agrupar y contar por causa de muerte y código
top_causas = (
    DAT_UNIDO_2.groupby(['MANERA_MUERTE', 'COD_3_CARCT'])
    .size()
    .reset_index(name='Total_casos')
    .sort_values(by='Total_casos', ascending=False)
    .head(10)
)

# Crear tabla interactiva
fig5 = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Manera de muerte</b>', '<b>Código</b>', '<b>Total de casos</b>'],
        fill_color='#1f77b4',
        font=dict(color='white', size=13),
        align='center'
    ),
    cells=dict(
        values=[
            top_causas['MANERA_MUERTE'],
            top_causas['COD_3_CARCT'],
            top_causas['Total_casos']
        ],
        fill_color=[['#f2f2f2', 'white']*5],  # alterna colores para mejor legibilidad
        align='center',
        font=dict(size=12)
    )
)])

# Ajustar título y diseño general
fig5.update_layout(
    title={
        'text': '10 principales causas de muerte<br>Colombia, año 2019',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 16}
    },
    height=500,
    margin=dict(t=100, b=50)
)

# Mostrar tabla
fig5.show()
############################
##### gráfico 6: BARRAS APILADAS ####
##############################

# Agrupar datos por departamento y sexo
muertes_sexo_depto = (
    DAT_UNIDO_2.groupby(['DEPARTAMENTO', 'SEXO'])
    .size()
    .reset_index(name='Total_muertes')
)

# Reemplazar valores de sexo por texto descriptivo
muertes_sexo_depto['SEXO'] = muertes_sexo_depto['SEXO'].replace({
    1: 'Masculino',
    2: 'Femenino',
    3: 'Indeterminado'
})

# Crear gráfico de barras apiladas
fig4 = px.bar(
    muertes_sexo_depto,
    x='DEPARTAMENTO',
    y='Total_muertes',
    color='SEXO',
    title='Comparación del total de muertes por sexo<br>en cada departamento - Colombia 2019',
    color_discrete_sequence=['#1f77b4', '#ff7f0e', '#8c564b']  # Azul, naranja y marrón suave
)

# Ajustar diseño general
fig4.update_layout(
    barmode='stack',
    xaxis_title='Departamento',
    yaxis_title='Número de muertes',
    title={
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 16},   # 🔹 Tamaño de título moderado
        'y': 0.95
    },
    legend=dict(
        orientation='h',       # Leyenda horizontal
        yanchor='bottom',
        y=1.05,                # 🔹 Arriba del gráfico
        xanchor='center',
        x=0.5
    ),
    height=600,
    plot_bgcolor='white',
    margin=dict(t=150, b=100)
)

# Reducir el tamaño de la fuente del eje X (departamentos)
fig4.update_xaxes(
    tickfont=dict(size=9)      # 🔹 Letra más pequeña en etiquetas de eje X
)

# Mostrar gráfico
fig4.show()

###############
####### Gráfico 7 histograma
##################

# Crear una copia de la base para no modificar la original
df_edades = DAT_UNIDO_2.copy()

# Definir los intervalos y etiquetas basados en los códigos DANE
bins = [-1, 4, 6, 8, 10, 11, 13, 16, 19, 24, 28, 29]  # límites
labels = [
    "Mortalidad neonatal (<1 mes)",
    "Mortalidad infantil (1-11 meses)",
    "Primera infancia (1-4 años)",
    "Niñez (5-14 años)",
    "Adolescencia (15-19 años)",
    "Juventud (20-29 años)",
    "Adultez temprana (30-44 años)",
    "Adultez intermedia (45-59 años)",
    "Vejez (60-84 años)",
    "Longevidad / Centenarios (85+ años)",
    "Edad desconocida"
]

# Crear variable categórica basada en los intervalos
df_edades["GRUPO_EDAD_CAT"] = pd.cut(
    df_edades["GRUPO_EDAD1"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# 2. Calcular la distribución (conteo de muertes)
dist_edad = (
    df_edades["GRUPO_EDAD_CAT"]
    .value_counts()
    .reset_index()
)

# Renombrar columnas según los nombres reales
dist_edad.columns = ["Grupo de edad", "Total_muertes"]

# Ordenar las categorías en el orden lógico del DANE
dist_edad["Grupo de edad"] = pd.Categorical(
    dist_edad["Grupo de edad"],
    categories=[
        "Mortalidad neonatal (<1 mes)",
        "Mortalidad infantil (1-11 meses)",
        "Primera infancia (1-4 años)",
        "Niñez (5-14 años)",
        "Adolescencia (15-19 años)",
        "Juventud (20-29 años)",
        "Adultez temprana (30-44 años)",
        "Adultez intermedia (45-59 años)",
        "Vejez (60-84 años)",
        "Longevidad / Centenarios (85+ años)",
        "Edad desconocida"
    ],
    ordered=True
)

dist_edad = dist_edad.sort_values("Grupo de edad")

#3. Creo el histograma
fig7 = px.bar(
    dist_edad,
    x="Grupo de edad",
    y="Total_muertes",
    text="Total_muertes",
    color="Grupo de edad",
    title="Distribución de muertes por grupo etario<br>Colombia, año 2019",
)

# Ajustes estéticos
fig7.update_traces(textposition="outside")
fig7.update_layout(
    title={
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 14}
    },
    xaxis_title="Grupo de edad",
    yaxis_title="Número de muertes",
    showlegend=False,
    height=600
)

fig7.show()
