import signal
import sys

def fermer_programme(signal, frame):
    """ Fonction appelee quand vient l'heure de fermer notre
    programme"""
    print(" C'est l'heure de la fermeture !")
    print("Sigint is ", signal)
    sys.exit(0)

signal.signal(signal.SIGINT, fermer_programme)

print("the program will loop")
while True:
    continue
