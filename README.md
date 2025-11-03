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
