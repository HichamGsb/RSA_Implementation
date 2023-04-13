from functions import *

# ---- Test 2 : Clef de petite taille ----
n = 755918011
p, q = factorisation(n)
phi_n = calculer_phi_n(p, q)
e = 163119273
d = inversion_modulaire(e, phi_n)

cle_privee = (d,n)
cle_publique = (e,n)

print("Test avec une clef de petite taille :")
print("n = ", n)
print("p = ", p)
print("q = ", q)
print("phi_n = ", phi_n)

print("Clef publique = ", cle_publique)
print("Clef privée = ", cle_privee)

message_chiffre = [671828605, 407505023, 288441355, 679172842, 180261802]
message_attendu = [3924, 2329, 6251, 3649, 4438]

test_passed = True

for i in range(len(message_chiffre)):
    msg_dechiffre = chiffrer_dechiffrer(message_chiffre[i], cle_privee)
    if(msg_dechiffre != message_attendu[i]):
        test_passed = False
        break

if(test_passed):
    print("Test passed")
else:
    print("Test failed")