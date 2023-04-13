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
print()

# ---------------- CHIFFREMENT / DECHIFFREMENT ----------------
# Génération de la clé publique et de la clé privée
print("Test de chiffrement / déchiffrement :")
public_key, private_key = generate_keys(16)
print("Clef publique : ", public_key)
print("Clef privée : ", private_key)

# Espace de message
    # Rappel : 1 < message < n
espace_de_message = public_key[1] - 1

# Chiffrement d'un message
message = random.randint(1, espace_de_message)

msg_chiffre = chiffrer_dechiffrer(message, public_key)
msg_dechiffre = chiffrer_dechiffrer(msg_chiffre, private_key)

print("Message original: ", message)
print("Message chiffré: ", msg_chiffre)
print("Message déchiffré: ", msg_dechiffre)
print()

# ---------------- FACTORISATION ----------------
print("Test de factorisation :")
tableau = [6, 26 , 39 , 51 , 2471 , 2479 , 2141229473 , 2141229499 , 998845402120303 , 998845402120339 , 999993647341131 , 999993647341147 , 999999505837877, 999999505837879]
for i in tableau:
    print("n = ", i)
    p, q = factorisation(i)
    if (p == None) or (q == None) :
        print("Impossible de factoriser n")
        print()
    else :
        print("p = ", p)
        print("Test de primalite : " , test_de_primalite(p))
        print("q = ", q)
        print("Test de primalite : " , test_de_primalite(q))
        print()