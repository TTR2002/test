import random

nombre_devin = random.randint(1, 100)

print(f"Bienvenue dans le jeu de devinettes !")
print(f'Je pense à un nombre entre 1 et 100. Pouvez-vous le deviner ?')

essais = 0

while True:
    
    essais += 1
    nbre = int(input("Entrez votre devinette : "))
    if nbre + 10 < nombre_devin:
        print(f"nombre trop petit")
    elif nbre - 10 > nombre_devin:
        print(f"nombre trop grand")
    elif nbre < nombre_devin:
        print(f"nombre petit")
    elif nbre > nombre_devin:
        print(f"nombre grand")
    else:
        print(f"Bravo ! Vous avez deviné le nombre en {essais} essais.")
        break











# import random
# # Générer un nombre aléatoire entre 1 et 100
# nombre_a_deviner = random.randint(1, 100)
# essais = 0
# print("Bienvenue dans le jeu de devinettes !")
# print("Je pense à un nombre entre 1 et 100. Pouvez-vous le deviner ?")
# while True:
#    # Demander une entrée utilisateur
#    essai = int(input("Entrez votre devinette : "))
#    essais += 1
#    if essai < nombre_a_deviner:
#        print("Trop bas ! Essayez encore.")
#    elif essai > nombre_a_deviner:
#        print("Trop haut ! Essayez encore.")
#    else:
#        print(f"Bravo ! Vous avez deviné le nombre en {essais} essais.")
#        break
# # Générer un nombre aléatoire entre 1 et 100
# nombre_a_deviner = random.randint(1, 100)
# essais = 0
# print("Bienvenue dans le jeu de devinettes !")
# print("Je pense à un nombre entre 1 et 100. Pouvez-vous le deviner ?")
# while True:
#    # Demander une entrée utilisateur
#    essai = int(input("Entrez votre devinette : "))
#    essais += 1
#    if essai < nombre_a_deviner:
#        print("Trop bas ! Essayez encore.")
#    elif essai > nombre_a_deviner:
#        print("Trop haut ! Essayez encore.")
#    else:
#        print(f"Bravo ! Vous avez deviné le nombre en {essais} essais.")
#        break
    
