# Mortalidad en Colombia - Año 2019

Aplicación desarrollada en **Streamlit** para visualizar y analizar los datos de mortalidad en Colombia durante el año 2019, con base en los registros del DANE.

## Desarrollado por
**Jenny Marcela Patiño Aldana**  

Proyecto académico para la Maestría en Inteligencia Artificial (Universidad de La Salle)

## Introducción
Mediante este ejercicio se busca realizar gráficos interactivos en python por medio de la librería ploty, una vez realizados se realizará un dashboard por medio de la página render la cuál nos permite conectar dashboards para publicarlos en la web.

## Objetivo
Por medio de este ejercicio se busca analizar un set de datos de la mortalidad en Colombia para el año 2019, donde tenemos datos por departamento y ciudad, el tipo de muerte, sexo de la persona fallecida, edad e información adicional como códigos de clasificación de acuerdo al tipo de muerte.
Se busca hacer gráficos para analizar el comportamiento de mortalidad por meses, por ciudad, por departamento, mediante gráficos realizados en python por medio de ploty y subidos a render para poder ser visualizados de manera web.

## Requisitos 
Las librerías usadas y las versiones requeridas son:
streamlit==1.39.0
pandas==2.2.2
numpy==1.26.4
openpyxl==3.1.5
plotly==5.24.1
requests==2.32.3
urllib3==2.2.2
geopandas==0.14.4

## Despliegue
Para garantizar la accesibilidad en línea de la aplicación, se realizó el despliegue utilizando la plataforma Render, una solución Platform as a Service (PaaS) que permite publicar aplicaciones web directamente desde un repositorio de GitHub.
A continuación, se detallan los pasos seguidos para el despliegue:

**1. Creación del repositorio en GitHub:**
Se creó un repositorio público en GitHub y se subieron todos los archivos del proyecto, incluyendo:

app.py (archivo principal de la aplicación Streamlit).

requirements.txt (listado de librerías necesarias).

.python-version (archivo donde se especificó la versión de Python 3.11.9).

README.md (documentación del proyecto).

Archivos adicionales como bases de datos en formato .xlsx.

**2. Configuración de Render: y se creó una cuenta.**

Desde el panel principal, se seleccionó la opción “New + → Web Service”.

Se conectó la cuenta de Render con GitHub y se eligió el repositorio del proyecto.

En la configuración del servicio se establecieron los siguientes parámetros:

Environment: Python 3.11.9

Start command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0

Build command: pip install -r requirements.txt

**3. Instalación de dependencias:**
Render ejecutó automáticamente la instalación de las librerías definidas en requirements.txt.
Durante este proceso se corrigieron errores de compatibilidad especificando la versión de Python mediante el archivo .python-version.

**4. Despliegue exitoso:**
Una vez completada la instalación, Render generó una URL pública para acceder a la aplicación en línea.
De esta forma, la aplicación puede visualizarse y ejecutarse desde cualquier navegador sin necesidad de ejecutar código localmente.

Se accedió a https://render.com
## Software
Todo el desarrollo de código se hizo desde python bajo el programa de Visual Studio Code, y del desarrollo de la aplicación se hizo desde la página de Render, y se usó GitHub para subir todos los archivos del repositorio.

## Instalación

Para ejecutar la aplicación de manera local, se deben seguir los siguientes pasos:

**1. Clonar el repositorio del proyecto:**
Acceder al repositorio en GitHub y copiar la URL del mismo.
Luego, abrir una terminal o el Anaconda Prompt y ejecutar:
git clone https://github.com/JennyP-M/mortalidad-colombia-streamlit

**2. Acceder al directorio del proyecto:**
Una vez clonado, ingresar a la carpeta del proyecto con el comando:
mortalidad-colombia-streamlit

**3.(Opcional) Crear y activar un entorno virtual:**
Este paso permite aislar las dependencias del proyecto.

**4. Instalar las dependencias necesarias:**
Instalar todas las librerías requeridas desde el archivo requirements.txt:
pip install -r requirements.txt

**5. Ejecutar la aplicación Streamlit:**
Una vez completada la instalación, ejecutar el siguiente comando:
streamlit run app.py
Esto iniciará la aplicación en un servidor local y mostrará un enlace del tipo:
http://localhost:8501
Al abrirlo en el navegador, se podrá visualizar la aplicación de forma interactiva.

## Visualizaciones con explicaciones de los resultados
Una vez ya desplegado el Dashboard vamos a tener las siguientes imagenes:
**Distribución total de muertes por departamento (2019)**
El gráfico del mapa de Colombia representa un mapa de calor donde se marca más los departamentos con una tasa de mortalidad más alta, vemos que el que más resalta es Bogotá con 5.280 muertes solo en el añ 2019, seguido de Antioquia con 1.504 y Valle del Cauca con 1.310. Tiene bastante sentido que se marquen más estas zonas ya que son estos departamentos donde quedan las ciudades principales de Colombia y donde se va a acumular más personas.

<img width="996" height="559" alt="imagen" src="https://github.com/user-attachments/assets/5a121e0d-735c-40d8-beb6-761e42b46490" />

**Total de muertes por mes**
En este segundo gráfico vemos el agregado del total de muertes por mes para todo el 2019 en Colombia. Curiosamente el mes con más muertes fue agosto con 2.784, me parece curioso ya que pensaba que los meses con más muertes podían ser diciembre o enero ya que es los meses donde la gente más viaja y puede haber una mayor tasa de accidentes. Aunque en el gráfico si vemos que aumenta en diciembre con 784, sin embargo no supera el mes de agosto.
<img width="1005" height="449" alt="imagen" src="https://github.com/user-attachments/assets/619e186e-bde1-4120-8b59-e067993593ab" />

**Los 5 departamentos con más muertes por homicidio**
En los municipios con más muertes por homicidio tenemos en primer lugar a Bogotá con 87 casos, seguido de Cali con 64, y vemos que los últimos 3 municipios, Cucuta, Tulua y Bucaramanga disminuyen bastante respecto a Cali y Bogotá, esto tiene sentido ya que Bogotá es la capital, tiene una densidad poblacional fuerte y por eso encabeza este top, y por otro lado Cali es una ciudad principal también, y se ha visto en distintos medios de comunicación que es una de las ciudades más peligrosas de Colombia. 
<img width="977" height="391" alt="imagen" src="https://github.com/user-attachments/assets/30e02a4d-edb8-405e-8565-a722b9b4ab77" />

**Los 10 municipios con menor mortalidad**
Los 10 municipios con menor mortalidad son: Yopal, Riosucio, Puerto Asis, Florida, Prado, Fonseca, Pitalito, Garzón, Espina, Gigante. Con solo 1 muerte registrada en todo el 2019, de esta gráfica me parece curioso que aparezca Yopal ya que es la capital de Casanare y al ser capital se puede concentrar mayor cantidad de personas y por ende tener una mayor tasa de mortalidad. Los demás municipios tiene sentido su comportamiento ya que son municipios pequeños y van a tener menos población. 
<img width="988" height="340" alt="imagen" src="https://github.com/user-attachments/assets/d6e8f5be-334c-420b-86fe-2271b7451a74" />

**10 principales causa de muerte**

Si revisamos las 10 principales causas de muerte de acuerdo a su código de dos cifras, tenemos que mayoritariamente es natural, ya que en este tipo se clasifican varios tipos de muerte como por ejemplo por enfermedad y se especifica el tipo de enfermedad dentro de la base, por eso vemos que abarca casi toda la tabla. Adicional tenemos también la muerte por homicidio la cuál tiene un total de 190 casos. 
<img width="755" height="404" alt="imagen" src="https://github.com/user-attachments/assets/6f8bd7db-9b05-4231-ae5e-cf4760a0df3e" />

**Comparación de muerte de sexo**
En la comparación de muerte por sexo y departamento, en Bogotá está casi a un 50-50 la mortalidad por género, en hombres tenemos 2.679 casos y en mujeres 2.599, en Antioquia vemos mayor cantidad de muertes en hombres sin embargo no es una diferencia fuerte, tenemos 867 casos de hombres y 637 de mujeres. En Valle del cauca también tenemos más casos en hombres pero nuevamente no es una diferencia fuerte respecto a las mujeres, tenemos 727 casos de hombres y 583 de mujeres. Estos son los departamentos que más resaltan ya que el resto de departamentos tiene un valor muy bajo y no se aprecia correctamente la comparación. 


<img width="843" height="559" alt="imagen" src="https://github.com/user-attachments/assets/6bd7684c-b63b-4dc0-ae90-abbb2ed6269b" />

**Distribución de mortalidad por grupo etario**
Para este grafico se crearon agrupaciones de acuerdo a la edad, y tenemos que el grupo con mayor mortalidad es vejez(60-84 años) lo cuál tiene mucho sentido, el siguiente es longevidad (más de 85) lo cuál también se entiende que por ser personas con edad más avanzada tiene mayor frecuencia, los grupos con menor frecuencia son los infantiles de 1 hasta los 14 años, aunque la neonatal si tiene más frecuencia que el resto de grupos infantiles, esto tiene sentido ya que son niños recien nacidos, pueden llegar a ser más débiles o haber desarrollado menos defensas. En si el gráfico es bastante lógico ya que va aumentando la frecuencia a medida que avanzan los grupos de edad.

<img width="841" height="557" alt="imagen" src="https://github.com/user-attachments/assets/6e744186-4e3c-4ce8-8164-c086c3a71d09" />



