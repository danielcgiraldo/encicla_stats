import time
import requests
from datetime import datetime
import json

def main():
    """
    Downloads the data from the API every minute and registers it in a csv.
    :return: None
    """
    f = open("stations.json")
    temp = json.load(f)

    fecha = str(datetime.now()).split(" ")
    #if int(fecha[1][0:2]) < 7 or int(fecha[1][0:2]) >= 19:
    #    return
    url = "https://webapp.metropol.gov.co/wsencicla/api/Disponibilidad/GetDisponibilidadMapas"
    response = requests.request("GET", url)
    stations = response.json()
    flag = False
    for key, value in temp.items():
        station = stations[int(key)]
        if station["bikes"] != value:
            
            archivo = open("data.txt", "a") # Make and/or open file
            archivo.write(str(station["name"])+","+ str(station["bikes"])+","+fecha[0]+","+fecha[1][0:8]+"\n")
            temp[key] = station["bikes"]
            archivo.close()
            flag = True
    f.close()

    if flag:
        with open("stations.json", "w") as outfile:
            json.dump(temp, outfile)


if __name__ == '__main__':
    main()
