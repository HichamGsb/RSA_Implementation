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
u, v, pgcd, reste = algo_euclide_etendu(a, b)
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