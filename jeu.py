

import os
import affichage_pendu
import random

def init() -> list:
    liste_de_mots = init_liste_de_mots()
    
    affichage_pendu.affichage(6)
    print("")
    print("Bienvenu dans le \"jeu du pendu\" !")
    print("")
    print('''Voici les règles et commandes :
Le "jeu du Pendu" est un jeu de devinettes dans lequel le joueur tente de deviner un mot choisi par l'ordinateur,
lettre par lettre, en un nombre limité d'essais.

- A chaque tour de jeu, le joueur donne une seule lettre pour trouver le mot
- s'il réussit alors la lettre est afficher
- si la lettre ne figure pas dans le mot, alors une partie du dessin du pendu est affiché
- le jeu s'arrête quand le joueur a découvert tout le mot (PARTIE GAGNEE) ou s'il a utilisé toutes ses chances (PARTIE PERDUE)
- A TOUT MOMENT, le joueur peut écrire la commande "quit" pour sortir du jeu
''')

    return liste_de_mots


def init_liste_de_mots() -> list:
    liste_de_mots = []

    with open("liste_de_mots.txt") as liste_de_mots_txt:
        for mot in liste_de_mots_txt:
            liste_de_mots.append(mot.replace("\n", ""))
    
    return liste_de_mots


def init_nouvelle_partie(liste_de_mots: list):
    mot = liste_de_mots[random.randint(0, len(liste_de_mots))]
    mot_a_trouver = []

    for lettre in mot:
        mot_a_trouver.append({"mystere": lettre, "valeur": "_"})

    return (0, 0, mot_a_trouver)


def nouveau_tour_de_jeu(nb_erreur: int, mot_a_trouver: dict, message: str):
    affichage_pendu.affichage(nb_erreur)
    affichage_mot_a_trouver = ""

    for lettre in mot_a_trouver:
        affichage_mot_a_trouver += lettre["valeur"] + " "
    
    print("")
    print("mot mystère :", affichage_mot_a_trouver)
    print("")
    print(message)
    print(f"nombre d'erreur : {nb_erreur}")


def afficher_le_mot(mot_a_trouver) -> str:
    mot = ""
    for lettre in mot_a_trouver:
        mot += lettre["mystere"]
    return mot