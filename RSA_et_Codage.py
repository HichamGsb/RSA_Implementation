from functions import *

# Génération d'un couple de clé privée / publique en fonction de la taille de la clé (modulo n) en bits
bits = 32
a, b = generate_keys(bits)
n = a[1]
print("a = ", a)
print("b = ", b)
print()

# On choisit un alphabet à 40 caractères 
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_",".","?","€","0","1","2","3","4","5","6","7","8","9"]
code = []

for i in range (0, len(alphabet)):
    code.append(i)

# Dictionnaire associant à chaque caractère un nombre
dictionnaire = dict(zip(code, alphabet))

# print("Dictionnaire :")
# print(dictionnaire)
# print(afficher_clef(dictionnaire, "0"))
# print(afficher_valeur(dictionnaire, 5))

# Calculer la taille du bloc de message
nombre_de_caracteres = len(dictionnaire)   # 40
print("Nombre de caractères : ", nombre_de_caracteres)
print()

x = calculer_taille_bloc(nombre_de_caracteres, n)
print("x =", x)