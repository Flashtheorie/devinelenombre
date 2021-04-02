#!//usr/bin/python
# -*- coding: UTF-8 -*-
import random 
import os


while True:
	argent = int(0)
	print("A vous de trouver le nombre entre 1 et 100");
	nombre = 0
	rand = random.randint(1,100)

	while rand != nombre:
		nombre = int(input("Votre choix ?"));
		if rand > nombre:
			print("Le nombre est plus grand")
		pass

		if rand < nombre:
			print("Le nombre est plus petit")
		pass

		if rand == nombre:
			print("Bravo !")
			argent = argent + 5
		pass
		if nombre == "hint":
			a = rand - 10
			b = rand + 10
			print("Le nombre est compris entre ", a, " et ", b)
			argent = argent - 10
			pass

	print("Vous avez " , argent , "€")

