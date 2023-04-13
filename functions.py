# Ce fichier contient les fonctions utilisées dans le programme principal.

import random
from math import sqrt

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
    if number == 2:
        return True
    elif number % 2 == 0:
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
        return a, 1, 0, 0
    elif(a % b == 0):
        return b, 0, 1, a % b
    else:
        pgcd, u, v, reste = algo_euclide_etendu(b, a % b)
        return pgcd, v, u - v * (a // b), reste
    
# ---------------- ALGORITHME D'EUCLIDE ETENDU SIMPLIFIE ----------------
def algo_euclide_etendu_simplifie(a, b):
    r = a
    r_prime = b
    u = 1
    v = 0
    u_prime = 0
    v_prime = 1
    while(r_prime != 0):
        q = r // r_prime
        rs, us, vs = r, u, v
        r, u, v = r_prime, u_prime, v_prime
        r_prime = rs - q * r_prime
        u_prime = us - q * u_prime
        v_prime = vs - q * v_prime
    return r, u, v

# ---------------- GENERATION D'UN NOMBRE PREMIER X où [2 < X < 2^bit_size] ----------------
# OBJECTIF : Géneration d'un nombre premier compris entre 2 et 2^bit_size
# Rappel : Il faut générer deux nombres premiers de l'ordre de a bits pour obtenir un module n de taille 2a bits
def generer_nombre_premier(bit_size):
    valeur_max = 2**(bit_size)
    while True:
        x = random.randint(2,valeur_max)
        if test_de_primalite(x):
            return x
        
# ---------------- INVERSION MODULAIRE ----------------
# Objectif : Améliorer la compréhension du code (simplification de retour de u)
def inversion_modulaire(a, n):
    pgcd, u, v, reste = algo_euclide_etendu(a, n)
    
    # Tant que u est négatif, on ajoute n à u
    while u < 0:
        u = u + n
    return u

# ---------------- GENERATION D'UNE PAIRE DE CLES PUBLIQUE / PRIVEE ----------------
# OBJECTIF : Générer une paire de clés (clé publique, clé privée) en fonction de la taille de la clé (modulo n) en bits
def generate_keys(bits):
    # Il faut générer deux nombres premiers de l'ordre de a bits pour obtenir un module n de taille 2a bits
    # On génère donc deux nombres premiers de l'ordre de n_prime = a/2 bits
    factor_bit_size = bits//2
    p = generer_nombre_premier(factor_bit_size)
    q = generer_nombre_premier(factor_bit_size)
    while p == q:
        p = generer_nombre_premier(factor_bit_size)
        
    n = p * q
    phi_n = calculer_phi_n(p, q)

    # Choisir e tel que 2 < e < phi(n) et PGCD(e, phi(n)) = 1
    while True:
        e = random.randint(2, phi_n)
        if(pgcd(e, phi_n) == 1):
            break

    # Calculer d tel que e.d + k.phi(n) = 1
    d = inversion_modulaire(e, phi_n)

    return ((e, n), (d, n))

# ---------------- CHIFFREMENT / DECHIFFREMENT ----------------
# OBJECTIF : Chiffrer / Déchiffrer un message grâce à l'exponentiation modulaire
# Rappels :
    # C = M^e mod n
    # M = C^d mod n
def chiffrer_dechiffrer(message, cle):
    u, n = cle
    message_prime = pow(message, u, n)
    return message_prime

# ---------------- CALCUL DE PHI(n)----------------
def calculer_phi_n(p, q):
    return (p - 1) * (q - 1)

# ---------------- FACTORISATION ----------------
# Il s'agit là  d'un algorithme simple de brut force
# Tout diviseur de n doit être inférieur ou égal à sa racine carrée.
def factorisation(n):
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return i, n // i
    return None, None

# ---------------- MANIPULATION D'UN DICTIONNAIRE ----------------
def afficher_clef(dictionnaire, x):
    for clef, valeur in dictionnaire.items():
        if valeur == x:
            return clef

def afficher_valeur(dictionnaire, x):
    for clef, valeur in dictionnaire.items():
        if clef == x:
            return valeur