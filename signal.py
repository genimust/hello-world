import signal
import sys
import keyboard


def fermer_programme(signal, frame):
    """ Fonction appelee quand vient l'heure de fermer notre
    programme"""
    print(" C'est l'heure de la fermeture !")
    print("Sigint is ", signal)
    sys.exit(0)

def show_key_pressed():
    print("keyboard pressed")


show_key_pressed()

signal.signal(signal.SIGINT, fermer_programme)

print("the program will loop")
while True:
    continue

signal.signal

if keyboard.
