import random
# Générer un nombre aléatoire entre 1 et 100
nombre_a_deviner = random.randint(1, 100)
essais = 0
print("Bienvenue dans le jeu de devinettes !")
print("Je pense à un nombre entre 1 et 100. Pouvez-vous le deviner ?")
while True:
   # Demander une entrée utilisateur
   essai = int(input("Entrez votre devinette : "))
   essais += 1
   if essai < nombre_a_deviner:
       print("Trop bas ! Essayez encore.")
   elif essai > nombre_a_deviner:
       print("Trop haut ! Essayez encore.")
   else:
       print(f"Bravo ! Vous avez deviné le nombre en {essais} essais.")
       break
# Générer un nombre aléatoire entre 1 et 100
nombre_a_deviner = random.randint(1, 100)
essais = 0
print("Bienvenue dans le jeu de devinettes !")
print("Je pense à un nombre entre 1 et 100. Pouvez-vous le deviner ?")
while True:
   # Demander une entrée utilisateur
   essai = int(input("Entrez votre devinette : "))
   essais += 1
   if essai < nombre_a_deviner:
       print("Trop bas ! Essayez encore.")
   elif essai > nombre_a_deviner:
       print("Trop haut ! Essayez encore.")
   else:
       print(f"Bravo ! Vous avez deviné le nombre en {essais} essais.")
       break