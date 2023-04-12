# Ce fichier contient les fonctions utilisées dans le programme principal.

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