import math
import random

print("Bienvenue au casino")
# situation de depart
pognon=input("T'as combien sur toi?")
pognon=int(pognon)
encore=True

#Debut du jeu
while pognon > 0 and encore == True:
	# Tu veux jouer a quoi?
	print("tu veux parier sur quoi?")
	print("pair/impair => tape p")
	print("numero => tape n")
	pari=input("p/n")
	# Calcul des gains/pertes
	if pari == "n":
		guess=input("Tu mises sur quel nombre entre 0 et 49?")
		guess=int(guess)
		print("Tu as parie sur la case", guess)
		mise=input("Tu mises combien?")
		if mise > pognon:
			print("La maison ne fait pas credit")
		destin=random.randrange(49)
		if guess == destin:
			print("T'as gagne mon gars!")		
			pepettes+=4*mise
		else:
			pognon-=mise
			print("C'est pas de bol!")
	elif pari == "p":
		guess=input("Tu mises sur pair ou impair? (p/i)")
		print("Tu as mise sur", guess)
		mise=input("Tu mises combien?")
		mise=int(mise)		
		if mise > pognon:
			print("La maison ne fait pas credit")
		destin=random.randrange(49)
		if destin%2 == 0:
			if guess == 'p':
				print("T'as gagne mon gars")
				pognon+=ceil(1.5*mise)
			else:
				print("C'est pas de bol!")
				pognon-=mise
		else:
			if guess == 'i':
				print("T'as gagne mon gars!")
				pognon+=ceil(1.5*mise)
			else:
				print("C'est pas de bol!")
				pognon-=mise
	else:
		print("jeu pas dasn la liste")
	# Meme joueur joue encore?
	encore=input("Tu veux encore jouer? (o/n)")
	if encore == "o":
		encore=True
	else:
		encore=False
	# Evaluation du pognon restant. Si banqueroute, fin du jeu	
	if pognon <= 0:
		print("C'est la banqueroute, mec!")
#Si banqueroute ou plus envie de jouer, on sort de la boucle
print("Le casino vous remercie de votre visite")
print("Tu repars avec ", pognon, "pieces d'or en poche.")
