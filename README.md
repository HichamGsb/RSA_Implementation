# RSA IMPLEMENTATION

## __Généralités__

### __But du projet :__ *Implémentation du cryptage à clé publique/privé RSA.*

*Le code est intensément commenté de façon à ce qu'il puisse être compris aisément. \
Ce Readme a été résumé au maximum, pour plus de détails sur une fonction, veuillez vous référez au code et au commentaires associés.*

*Afin de mieux comprendre la chronologie du projet, et les réfléxions associées, je vous recommande de vous référer aux commits associés au projet.*

---

Le projet est divisé en 3 parties :

1. Implémentation des fonctions arithmétiques nécessaires.
2. Génération de clés RSA de grande taille et test du fonctionnement de chiffrement et déchiffrement RSA.
3. Cryptage et décryptage des messages via un alphabet à 40 lettres.

---

Les programmes sont exécutables avec la commande `python3 <nom_du_fichier.py>`.

|Nom du fichier|Description|
|:---:|:---:|
|`functions.py`|Regroupe toutes les fonctions nécessaires aux programmes.|
|`tests.py`|Les tests unitaires associés à chaque fonction.|
|`small_key_test1.py`|Test avec une clé de petite taille (simple).|
|`small_key_test2.py`|Test avec une clé de petite tailel (plus ardu).|
|`RSA_et_Codage.py`|Ajout du cryptage et décryptage grâce à un alphabet.|

---

## __Détails sur les programmes__

### __Fonctions :__ `functions.py`

*Regroupe toutes les fonctions nécessaires au projet, pour plus de détails, veuillez vous réferrez au code et aux commentaires associés.*

1. __Arithmétiques__
    - PGCD
    - Test de primalité
    - Inversion modulaire
    - Exponentiation modulaire
    - Factorisation
    - Calcul de phi(n)
    ---

2. __RSA__
    - Génération de clés
    - Chiffrement
    - Déchiffrement
    ---

3. __Codage__
    - Manipulation de dictionnaires
    - Manipulation de listes
    - Codage
    - Décodage

---

### __Tests unitaires :__ `tests.py`

*Réalise des tests unitaires sur les fonctions développés dans `functions.py`.*

Un print est effectué pour chaque test de manière à faciliter la lecture des résultats.

---

### __Tests avec clés de petite taille :__ `small_key_test1.py` & `small_key_test2.py`

*Permet de tester les fonctions avec des clés de petite taille.*

__small_key_test1.py :__ Déchiffrement simple (e=12413 ; n=13289)

- *Message crypté :* [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356, 5356, 1159, 10280, 12523, 7506, 6311]
- *Message attendu :* [5424, 6221, 2423, 1662, 1023, 1362, 2917, 1023, 2028, 6215, 2427, 6210, 2121, 6229, 1714, 6215, 1828, 1762]

__small_key_test2.py :__ Déchiffrement plus ardu (e=163119273; n=755918011)

- *Message crypté :* [671828605, 407505023, 288441355, 679172842, 180261802]
- *Message attendu :* [3924, 2329, 6251, 3649, 4438]

Les programmes vérifient eux même que le message déchiffré est bien égal au message attendu via une boucle for.

---

### __Ajout du cryptage et décryptage d'un message :__ `RSA_et_Codage.py`

*Le but de cette partie est d'abord de simuler l'envoie d'un message entre deux personnes (Alice et Bob) en ajoutant le cryptage et le décryptage d'un message au chiffrement et déchiffrement RSA.*

- Alice veut envoyer un message à Bob, mais elle ne veut pas que ce message soit lisible par n'importe qui.\
    -> Crypter un message grâce à un alphabet

- Elle va donc crypter son message grâce à la clé publique de Bob, et lui envoyer.\
    -> Chiffrer le message crypté

- Bob va ensuite décrypter le message grâce à sa clé privée.\
    -> Déchiffrer le message

- Le message est alors déchiffré, mais il est toujours crypté.\
    -> Décrypter le message.

Dans le code, les parties cryptages et décryptages reposent sur la manipulation d'un dictionnaire où chaque lettre est associée à un nombre.

__Alphabet :__ `ABCDEFGHIJKLMNOPQRSTUVWXYZ_.?€0123456789` \
__Taille :__ 40
