# Meteorological_station_Quito
This is a meteorological Station in Quito using Python and the Free IoT platform www.thinkspeak.com

Proyecto estacion meteorologica en quito con thinkspeak
Version: 1.0
Autor: Ing. Ronny Diaz Lopez
F. Creado: Jueves, 28-07-2022
Coding: Python 3.8.10 (Entorno Virtual)
Objetivo: Crear una estacion meteorologica que visualice en tiempo real los datos de: Temperatura (Grados celcius(, Humedad relativa (%), Velocidad del viento (Km/h), Nivel de lluvia (mm) y Radiacion Solar (W/m2), todo en tiempo real, a partir de los datos tomados del sitio meteorologico oficial de nuestro pais: Ecuador, usando la tecnica de Web Scrapping con Python.

Usaremos la plataforma gratuita thinkspeak.com
link: https://thingspeak.com/channels

Paso 1: Crea tu propio canal gratis en esta plataforma https://thingspeak.com/channels
Crearemos un canal thinkspeak mediante una API REST.

Vamos a crear y configurar un canal en ThingSpeak utilizando la API REST que facilita la plataforma, y código Python. Toda la documentación correspondiente y un conjunto de ejemplos podéis encontrarlos en el siguiente enlace: https://es.mathworks.com/help/thingspeak/rest-api.html

La arquitectura REST se basa en las peticiones GET, PUT, POST y DELETE del protocolo HTTP.

Paso 2: Creamos el Archivo .py con el codigo.
En primer lugar necesitamos crear un archivo con extensión .py, en el cual codificaremos la solución. A continuación, introducid las siguientes lineas en el archivo a fin de importar las librerías que vamos a necesitar.

Paso 3: Ejecutar el programa y abrir la plataforma thinkspeak.
Si todo esta bien codificado y configurado deberia verse tu canal con algo parecido a esto:
![image](https://user-images.githubusercontent.com/17863684/181649879-3bcd9162-01f8-43e2-b7c8-3da2e0f7d5f6.png)
