from functions import *

# Génération d'un couple de clé privée / publique en fonction de la taille de la clé (modulo n) en bits
bits = 32
clef_publique, clef_privee = generate_keys(bits)
n = clef_publique[1]
print("clef_publique =", clef_publique)
print("clef_privee =", clef_privee)
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
print("Nombre de caractères :", nombre_de_caracteres)
print()

taille_bloc = calculer_taille_bloc(nombre_de_caracteres, n)
print("taille_bloc =", taille_bloc)

# Codage : Transformer un texte en code
texte = "BONJOUR"
texte_chiffre = text_to_code(texte, dictionnaire)

# Décodage : Transformer un code en texte
texte_dechiffre = code_to_text(texte_chiffre, dictionnaire)

print("texte =", texte)
print("texte_chiffre =", texte_chiffre)
print("texte_dechiffre =", texte_dechiffre)
print()

# Decouper le message en blocs de taille x
print("Decoupage du message en blocs de taille", taille_bloc)
liste_blocs = decouper_message(texte, taille_bloc)
print(liste_blocs)