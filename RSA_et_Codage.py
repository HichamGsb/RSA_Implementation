from functions import *

# Génération d'un couple de clé privée / publique en fonction de la taille de la clé (modulo n) en bits
bits = 1024
a, b = generate_keys(64)
print("a = ", a)
print("b = ", b)