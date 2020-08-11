import signal

def lancer_programme(signal, frame):
    """"Fonction appelée quand vient l'heure de d'executer notre programme"""
    print("\nReceived signal")


# Connexion du signal à notre fonction
signal.signal(signal.SIGINT, lancer_programme)

while True :
    signal.pause()
    # Notre programme...
    print("the program starts its work")
    chaine = input("Give me the expected channel: ")
    chaine = chaine + "\n"
    with open('fichier.txt', 'a') as mon_fichier: #on enregistre la saisie dans un fichier
        mon_fichier.write(chaine)


