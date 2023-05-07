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
def recuperer_clef(dictionnaire, x):
    for clef, valeur in dictionnaire.items():
        if valeur == x:
            return clef

def recuperer_valeur(dictionnaire, x):
    for clef, valeur in dictionnaire.items():
        if clef == x:
            return valeur
        
# ---------------- CALCUL DE LA TAILLE DU BLOC ----------------
# OBJECTIF : Calculer la taille du bloc à partir du nombre de caractères du dictionnaire et de la taille en bits du modulo n
# Rappels :
    # Pour calculer la taille du bloc pour le message en clair, il faut déterminer le plus grand entier m tel que 40^m < n_bits.
    # Le bloc sera alors consitiué de m caractères.
def calculer_taille_bloc(nombre_de_caracteres, n):
    taille_bloc = 1
    x = nombre_de_caracteres**taille_bloc
    while(x < n):
        x = nombre_de_caracteres**taille_bloc
        taille_bloc += 1
    return taille_bloc - 2

# ---------------- TRANSFORMER UN TEXTE EN CHIFFRES ----------------
# CODAGE : Transformer un texte en chiffres
def text_to_code(texte, dictionnaire):
    liste_chiffres = []
    for i in texte:
        liste_chiffres.append(recuperer_clef(dictionnaire, i))
    return liste_chiffres

# DECODAGE : Transformer les chiffres en texte
def code_to_text(code, dictionnaire):
    liste_caracteres = []
    for i in code:
        liste_caracteres.append(recuperer_valeur(dictionnaire, i))
    return liste_caracteres

# ---------------- DECOUPER UN MESSAGE EN BLOCS DE TAILLE X ----------------
def decouper_message(message, taille_bloc):
    liste_blocs = []
    while(len(message) > taille_bloc):
        liste_blocs.append(message[:taille_bloc])
        message = message[taille_bloc:]
    liste_blocs.append(message)
    return liste_blocs

# ---------------- TRANSFORMER UNE LISTE DE BLOCS DE TEXTE EN UNE LISTE DE CHIFFRES ----------------
def text_blocs_list_to_int_blocs_list(liste_blocs, dictionnaire):
    liste_chiffres = []
    for i in liste_blocs:
        liste_chiffres.append(text_to_code(i, dictionnaire))
    return liste_chiffres

# ---------------- TRANSFORMER UNE LISTE DE BLOCS DE CHIFFRES EN UNE LISTE DE BLOCS DE TEXTE ----------------
def int_blocs_list_to_text_blocs_list(liste_blocs, dictionnaire):
    liste_texte = []
    for i in liste_blocs:
        liste_texte.append(code_to_text(i, dictionnaire))
    return liste_texte

# ---------------- REVERSE UNE LISTE DE LISTES ----------------
# Exemple : [[1, 14, 13, 9, 14], [20, 17]] -> [[14, 9, 13, 14, 1], [17, 20]]
def reverse_list(liste):
    liste_inverse = []
    for i in liste:
        liste_inverse.append(i[::-1])
    return liste_inverse

# ---------------- ENCODER UNE LISTE DE LISTES DE CHIFFRES SELON L'EMPLACEMENT DES CHIFFRES ----------------
# Exemple : "BONJOUR" associé à un dictionnaire de taille M (ici 40)
# BONJO -> 1 14 13 9 14 -> 14 9 13 14 1 -> 14*M**0 + 9*M**1 + 13*M**2 + 14*M**3 + 1*M**4
# UR    -> 20 17        -> 17 20        -> 17*M**0 + 20*M**1
def encoder(liste, nombre_de_caracteres):
    print("Nombre de caracteres :", nombre_de_caracteres)
    resultat = []  
    calcul_message = 0
    somme = 0
    for i in liste:
        x = 0
        for j in i:
            calcul_message = j * (nombre_de_caracteres**x)
            print("Chiffre en cours", j, ",", "Calcul", calcul_message)
            somme += calcul_message
            print("Somme", somme)
            x += 1
        resultat.append(somme)
        somme = 0
    return resultat

# ---------------- CHIFFREMENT/DECHIFFREMENT D'UNE LISTE DE MESSAGE EN UNE LISTE DE MESSAGE CHIFFRES ----------------
def chiffrer_dechiffrer_liste(liste, cle):
    liste_chiffree = []
    for i in liste:
        liste_chiffree.append(chiffrer_dechiffrer(i, cle))
    return liste_chiffree

# ---------------- DECODER UNE LISTE DE LISTES DE CHIFFRES SELON L'EMPLACEMENT DES CHIFFRES ----------------
def decoder(liste, nombre_de_caracteres):
    resultat = []
    for i in liste:
        message = []
        while i > 0:
            chiffre = i % nombre_de_caracteres
            message.append(chiffre)
            i = (i - chiffre) // nombre_de_caracteres
        resultat.append(list(reversed(message)))
    return resultat

# ---------------- TRANSORMER UNE LISTE DE LISTES DE CHIFFRES EN CHAINE DE CARACTERES ----------------
def concatener(liste):
    resultat = []
    for i in liste:
        for j in i:
            resultat.append(j)
    res = ""
    for i in resultat:
        res += str(i)
    return res