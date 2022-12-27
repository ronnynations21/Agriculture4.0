#**********************************************************************************************************************************************
# Nombre programa: read_send_datapy
# Version: 1.0
# F. Creado: Jueves, 28-07-2022
# Codigo: Python 3.8.10 (ambiente virtual en VS Code)
# Autor: Ing. Ronny Diaz Lopez
#
# Programa para leer y visualizar todos los datos de interes desde el sitio web meteorologico: https://www.meteoblue.com/es/tiempo/hoy/quito_ecuador_3652462
# En este caso leemos Temperatura, Humedad relativa, velocidad del viento, Radiacon solar y nivel de lluvia caida.
# Esto con el objetivo de crear una estacion meteorologica propia publica en la plataforma IoT thinkspeak.com para 
# contar con datos reales que uaremos en nuestro controlador climatico inteligente.
#
#**************************************************************************************************************************************

# IMportamos las librerias que vamos a utilizar
import pandas as pd
import thingspeak
import time
import re  # Me permite trabajar con expresiones regulares para poder convertir el valor string de la temp a entero

#*****************************   Modulo de envio de datos a la plataforma *****************************************************************************
# Para poder publicar los datos, en primer lugar es necesario crear el canal el que se van a publicar. Necesitamos la clave Write API Key y el 
# ID del canal en el que vamos a publicar los datos. 
Channel_Id=XXXXXXX # Colocar aqui tu ID de tu perfil
Write_API_Key='XXXXXXXXXXXXXXXXX' # POnemos aqui nuestra "WRITE API KEY"
User_API_Key='XXXXXXXXXXXXXXXXXX' # POnemos aqui nuestra "API KEY"

def send_data(channel, url_EC):
    #Se leen los datos del sitio web: https://www.meteoblue.com/es/tiempo/hoy/quito_ecuador_3652462
    datosweb=pd.read_html(url_EC)
    # Extraemos la Temperatura en grados celcius
    temp = datosweb[0][1][2]
    # Ahora como el valor de temp es un string tenemos que convertirlo a entero para poderlo graficar
    res="".join(re.split("°",temp))
    temp=int(res)
    print("Valor Temperatura es: ")
    print(temp)
    # Extraemos la Humedad Relativa en %
    hum = datosweb[0][1][7]
    # Extraemos la Direccion del viento
    wind_speed = datosweb[0][1][5]
    # Extraemos la lluvia en mm
    lluvia = datosweb[0][1][6]
    # Extraemos la radiacion solar en 
    solar = datosweb[0][1][0]
    # escritura del valor
    response = channel.update({'field1': temp, 'field2': hum, 'field3': wind_speed, 'field4': lluvia, 'field5': solar})
    
    
#************** Main Module ************************************************************************
if __name__ == "__main__":
    url_EC = 'https://www.meteoblue.com/es/tiempo/hoy/quito_ecuador_3652462'
    channel = thingspeak.Channel(id=Channel_Id, api_key=Write_API_Key)
    while True: 
        send_data(channel, url_EC)
        # una cuenta gratuita tiene una limitación en el API de 15sec
        time.sleep(15)
      
