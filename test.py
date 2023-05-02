import time
from datetime import datetime

def main():
    """
    Downloads the data from the API every minute and registers it in a csv.
    :return: None
    """
    
    fecha = str(datetime.now())
    archivo = open("test.txt", "a") # Make and/or open file
    archivo.write(fecha+"\n")
    archivo.close()


if __name__ == '__main__':
    main()
