import time
import requests
from datetime import datetime

def main():
    """
    Downloads the data from the API every minute and registers it in a csv.
    :return: None
    """

    temp = {
        9: -1, # Suramericana
        46: -1, # Parque de los enamorados
        93: -1, # Colombia
        97: -1, # Carlos E. Restrepo
        98: -1 # Campus Nacional Volador
    }

    i = 0

    while True:

        fecha = str(datetime.now()).split(" ")

        if int(fecha[1][0:2]) < 7 or int(fecha[1][0:2]) >= 19:
            i += 1
            print(f"Ciclo {i}")
            time.sleep(10)
            continue

        url = "https://webapp.metropol.gov.co/wsencicla/api/Disponibilidad/GetDisponibilidadMapas"

        response = requests.request("GET", url)

        stations = response.json()
        # Fecha en al que se tomo el dato
        

        # TODO: Save the data in a csv for suramericana and volador
        archivo = open("datos.txt", "a") #crear archivo
        
        for key, value in temp.items():
            if stations[key]["bikes"] != value:
                archivo.write(str(stations[key]["name"])+","+ str(stations[key]["bikes"])+","+fecha[0]+","+fecha[1][0:8]+"\n")
                temp[key] = stations[key]["bikes"]
        archivo.close()
        # Wait 10 seconds before next request
        i += 1
        print(f"Ciclo {i}")
        time.sleep(10)


if __name__ == '__main__':
    main()
