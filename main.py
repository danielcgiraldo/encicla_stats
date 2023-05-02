import time
import requests
from datetime import datetime

def main():
    """
    Downloads the data from the API every minute and registers it in a csv.
    :return: None
    """

    while True:

        url = "https://webapp.metropol.gov.co/wsencicla/api/Disponibilidad/GetDisponibilidadMapas"

        response = requests.request("GET", url)

        stations = response.json()
        # Fecha en al que se tomo el dato
        fecha = str(datetime.now()).split(" ")

        # TODO: Save the data in a csv for suramericana and volador
        archivo = open("datos.txt", "a") #crear archivo
        numeros = [9,46,93,97,98] #suramericana,parque de los enamorados, colombia, carlos_E, campus nacional
        for numero in numeros:
          archivo.write(str(stations[numero]["name"])+","+ str(stations[numero]["bikes"])+","+fecha[0]+","+fecha[1][0:8]+"\n")
        archivo.close()
        # Wait 1 minute before next request
        time.sleep(60)


if __name__ == '__main__':
    main()
