#!//usr/bin/python
# -*- coding: UTF-8 -*-
import random 
import os

argent = 0
while True:
	print("A vous de trouver le nombre entre 1 et 100");
	nombre = 0
	rand = random.randint(1,100)
	if type(nombre == int):
		while rand != nombre:
			nombre = int(input("Votre choix ? (0 pour un indice)"));
			if rand > nombre:
				print("Le nombre est plus grand")
			pass

			if rand < nombre:
				print("Le nombre est plus petit")
			pass

			if rand == nombre:
				print("Bravo !")
				argent = int(argent + 5) 
				print("Vous avez " , argent , "€")
			pass
			if nombre == 0:
				if argent >= 10:
					a = rand - 10
					b = rand + 10
					print("Le nombre est compris entre ", a, " et ", b)
					argent = argent - 10
					pass
				else:
					print("Vous n'avez pas assez d'argent.")

	

