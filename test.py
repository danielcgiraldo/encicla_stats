import time
import requests
from datetime import datetime

def main():

    i = 0

    while True:
        archivo = open("test.txt", "a") # Make and/or open file
        archivo.write(str(i)+"\n")
        archivo.close()
        i += 1
        time.sleep(10)


if __name__ == '__main__':
    main()
