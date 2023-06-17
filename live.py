import requests
from datetime import datetime
import json

def main():
    """
    Downloads the data from the API every minute and registers it in a csv.
    :return: None
    """

    url = "https://webapp.metropol.gov.co/wsencicla/api/Disponibilidad/GetDisponibilidadMapas"
    response = requests.request("GET", url)
    stations = response.json()
    station = stations[98]
    print("Bicicletas:", station["bikes"])
    print("Estado:", station["bikes_State"])

if __name__ == '__main__':
    main()
