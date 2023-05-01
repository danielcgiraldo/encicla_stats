import time
import requests

def main():
    """
    Downloads the data from the API every minute and registers it in a csv.
    :return: None
    """

    while True:

        url = "https://webapp.metropol.gov.co/wsencicla/api/Disponibilidad/GetDisponibilidadMapas"

        response = requests.request("GET", url)

        stations = response.json()
        # TODO: Save the data in a csv for suramericana and volador
        archivo = open("muu.txt", "a") #crear archivo
        archivo.write(str(stations[9]) +","+ str(stations[98])+"\n")
        archivo.close
        # Wait 1 minute before next request
        time.sleep(60)


if __name__ == '__main__':
    main()
