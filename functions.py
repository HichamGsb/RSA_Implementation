# Ce fichier contient les fonctions utilisées dans le programme principal.

import random

# ---------------- CALCUL DU PGCD ----------------
# OBJECTIF : Calculer le PGCD de deux entiers A et B.
def pgcd(a, b):
    if b == 0:
        # Si B est nul, on renvoie A
        return a
    else:
        # Sinon, on renvoie le PGCD de B et le reste de la division euclidienne de A par B
        return pgcd(b, a % b)

# ---------------- TEST DE PRIMALITE ----------------
# OBJECTIF : Déterminer si un nombre est premier ou non.
def test_de_primalite(number):
    # Si n est divisible par 2, il n'est pas premier
    if number % 2 == 0:
        return False
    # Si n n'est pas divisble par 2, on teste si n est divisible par un nombre impair compris entre 3 et la racine carrée de n
    else:
        for i in range(3, int(number ** 0.5) + 1, 2):
            # Si c'est le cas, n n'est pas premier
            if number % i == 0:
                return False
        return True
    
# ---------------- ALGORITHME D'EUCLIDE ETENDU ----------------
# OBJECTIFS : 
    # Inversion modulaire : trouver x tel que a.x mod n = 1
    # Calculer le PGCD de deux entiers A et B
    # Trouver une paire de coefficient (U et V) qui satisfait une relation de Bezout entre A et B

# Rappels :
    # PGCD(a, b) = PGCD(b, a % b)
    # Il existe k € phi(n) tel que e*d + k*phi(n) = 1
def algo_euclide_etendu(a, b):
    if b == 0:
        return 1, 0, a, 0
    elif(a % b == 0):
        return 0, 1, b, a % b
    else:
        u, v, pgcd, reste = algo_euclide_etendu(b, a % b)
        return v, u - v * (a // b), pgcd, reste