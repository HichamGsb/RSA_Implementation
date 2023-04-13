from functions import *

# ---- Test 1 : Clef de petite taille ----
n = 13289
p, q = factorisation(n)
phi_n = calculer_phi_n(p, q)
e = 12413
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

message_chiffre = [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356, 5356, 1159, 10280, 12523, 7506, 6311]
message_attendu = [5424, 6221, 2423, 1662, 1023, 1362, 2917, 1023, 2028, 6215, 2427, 6210, 2121, 6229, 1714, 6215, 1828, 1762]

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