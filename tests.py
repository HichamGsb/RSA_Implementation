from functions import *

# OBJECTIF DU PROJET : Implémenter le cryptage à clé publique/privé RSA.

# ---------------- CALCUL DU PGCD ----------------
print("Test PGCD :")
print(pgcd(11, 5))
print()

# ---------------- TEST DE PRIMALITE ----------------
print("Test de primalité :")
print(test_de_primalite(12))
print(test_de_primalite(7))
print()

# ---------------- ALGORITHME D'EUCLIDE ETENDU ----------------
print("Test de l'algorithme d'Euclide étendu :")
a = 11
b = 55
pgcd, u, v, reste = algo_euclide_etendu(a, b)
print("a = ", a)
print("b = ", b)
print("u = ", u)
print("v = ", v)
print("PGCD = ", pgcd)
print("Reste = ", reste)
print()

# ---------------- ALGORITHME D'EUCLIDE ETENDU SIMPLIFIE ----------------
print("Test de l'algorithme d'Euclide étendu simplifié :")
a = 11
b = 55
pgcd, u, v = algo_euclide_etendu_simplifie(a, b)
print("a = ", a)
print("b = ", b)
print("u = ", u)
print("v = ", v)
print("PGCD = ", pgcd)
print()

# ---------------- GENERATION D'UN NOMBRE PREMIER X où [2 < X < 2^bit_size] ----------------
print("Test de génération de nombres premiers :")
print(generer_nombre_premier(4))
print(generer_nombre_premier(4))
print()

# ---------------- GENERATION D'UNE PAIRE DE CLES PUBLIQUE / PRIVEE ----------------
print("Test de génération de clefs (e,n), (d,n):")
public_key, private_key = generate_keys(16)
print("Clef publique : ", public_key)
print("Clef privée : ", private_key)