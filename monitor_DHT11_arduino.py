import smbus
import time
import datetime
# commentaire
# remplacer 0 par 1 si nouveau raspberry pi
bus = smbus.SMBus(1)
address = 0x12

while True:
 # envoi d'un signal à l'arduino
 bus.write_byte(address, 3)

 # pause de 1 seconde pour laisser le temps de traitement
 time.sleep(1)
 reponse = bus.read_byte(address)

 # affichage de la température
 print("La température est de:", reponse, "°C")

 # ecriture de la réponse dans un fichier
 reponse = str(reponse)
 fichier = open("temp_history.txt", "a")
 date = datetime.datetime.now()
 date = str(date)
 fichier.write(date)
 fichier.write("\t")
 fichier.write(reponse)
 fichier.write("\n")
 fichier.close()

 # Attente d'une minute avant de relancer une mesure
 time.sleep(59)
