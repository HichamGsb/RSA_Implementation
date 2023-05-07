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

# Découper le message clair en blocs
print("Decoupage du message en blocs de taille", taille_bloc)
liste_blocs = decouper_message(texte, taille_bloc)
print(liste_blocs)
print()

# Transformer une liste de blocs en liste de chiffres
# Valeur -> Clef
# Exemple : "BONJOUR" en taille de bloc M
# BONJO -> 1 14 13 9 14
# UR    -> 20 17
print("Transformation d'une liste de blocs en liste de chiffres")
liste_clefs = text_blocs_list_to_int_blocs_list(liste_blocs, dictionnaire)
print(liste_clefs)
print()

# Reverse la liste pour pouvoir utiliser les indices en guise d'exponentiel
# [[1, 14, 13, 9, 14], [20, 17]] -> [[14, 9, 13, 14, 1], [17, 20]]
print("Reverse")
liste_clefs = reverse_list(liste_clefs)
print(liste_clefs)
print()

# Encodage : Transformer une liste de listes de chiffres selon l'emplacement des chiffres
# Exemple : "BONJOUR" associé à un dictionnaire de taille M (ici 40)
# BONJO -> 1 14 13 9 14 -> 14 9 13 14 1 -> 14*M**0 + 9*M**1 + 13*M**2 + 14*M**3 + 1*M**4
# UR    -> 20 17        -> 17 20        -> 17*M**0 + 20*M**1

# BONJO chiffré = 3477174
# UR chiffré = 817
print("Encodage")
liste_encodee = encoder(liste_clefs, nombre_de_caracteres)
print(liste_encodee)
print()

# Chiffrer la liste en une autre liste
print("Chiffrement de la liste")
liste_chiffree = chiffrer_dechiffrer_liste(liste_encodee, clef_publique)
print(liste_chiffree)
print()

# Déchiffrer la liste en une autre liste
print("Déchiffrement de la liste")
liste_dechiffree = chiffrer_dechiffrer_liste(liste_chiffree, clef_privee)
print(liste_dechiffree)
print()

print("Décodage")
liste_decodee = decoder(liste_dechiffree, nombre_de_caracteres)
print(liste_decodee)
print()

print("Liste de chiffres en liste de caractères (grâce au dictionnaire)")
liste_decodee_en_liste_de_lettres = int_blocs_list_to_text_blocs_list(liste_decodee, dictionnaire)
print(liste_decodee_en_liste_de_lettres)

# Liste de caractères -> Chaîne de caractères
message_decode_string = concatener(liste_decodee_en_liste_de_lettres)
print(message_decode_string)