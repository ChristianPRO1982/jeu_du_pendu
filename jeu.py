

import time
import os
import affichage_pendu
import random

def init() -> list:
    liste_de_mots = init_liste_de_mots()
    
    affichage_pendu.affichage(11,11)
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
    liste_de_mots_faciles = []
    liste_de_mots_moyens = []
    liste_de_mots_difficiles = []

    with open("liste_de_mots_faciles.txt") as liste_de_mots_txt:
        for mot in liste_de_mots_txt:
            liste_de_mots_faciles.append(mot.replace("\n", ""))
    with open("liste_de_mots_moyens.txt") as liste_de_mots_txt:
        for mot in liste_de_mots_txt:
            liste_de_mots_moyens.append(mot.replace("\n", ""))
    with open("liste_de_mots_difficiles.txt") as liste_de_mots_txt:
        for mot in liste_de_mots_txt:
            liste_de_mots_difficiles.append(mot.replace("\n", ""))
    
    return (liste_de_mots_faciles, liste_de_mots_moyens, liste_de_mots_difficiles)


def init_nouvelle_partie(liste_de_mots_faciles, liste_de_mots_moyens, liste_de_mots_difficiles):
    print("")
    difficulte = input("difficulté [1 = facile (défaut) / 2 = moyen / 3 = difficile] : ")
    if difficulte == '2':
        nb_erreur_max = 8
        liste_de_mots = liste_de_mots_moyens
    elif difficulte == '3':
        nb_erreur_max = 10
        liste_de_mots = liste_de_mots_difficiles
    else:
        nb_erreur_max = 7
        liste_de_mots = liste_de_mots_faciles
        
    mot = liste_de_mots[random.randint(0, len(liste_de_mots))]
    mot_a_trouver = []

    for lettre in mot:
        mot_a_trouver.append({"mystere": lettre.lower(), "MSA": lettre.lower(), "valeur": "_"}) # MAS Mystere Sans Accent

    for lettre in [["é","e"],
                   ["è","e"],
                   ["ê","e"],
                   ["ë","e"],
                   ["à","a"],
                   ["ï","i"],
                   ["î","i"],
                   ["ù","u"]]:
        mot_a_trouver = list(map(lambda lettre_a_touver: {"mystere": lettre_a_touver["mystere"], "MSA": lettre[1], "valeur": "_"}
            if lettre_a_touver["mystere"] == lettre[0] else
            {"mystere": lettre_a_touver["mystere"], "MSA": lettre_a_touver["MSA"], "valeur": "_"}, mot_a_trouver))

    return (0, time.time(), nb_erreur_max, mot_a_trouver)


def nouveau_tour_de_jeu(nb_erreur: int, nb_erreur_max: int, mot_a_trouver: dict, message: str):
    affichage_pendu.affichage(nb_erreur, nb_erreur_max)
    affichage_mot_a_trouver = ""

    for lettre in mot_a_trouver:
        affichage_mot_a_trouver += lettre["valeur"] + " "
    
    print("")
    print("mot mystère :", affichage_mot_a_trouver)
    print("")
    print(message)
    print(f"nombre d'erreur : {nb_erreur} sur {nb_erreur_max}")


def afficher_le_mot(mot_a_trouver) -> str:
    mot = ""
    for lettre in mot_a_trouver:
        mot += lettre["mystere"]
    return mot


def test_victoire(mot_a_trouver) -> bool:
    for lettre in mot_a_trouver:
        if lettre["valeur"] == "_":
            return False
    return True


def fin_jeu(nb_erreur, nb_erreur_max, mot_a_trouver, message, liste_de_mots_faciles, liste_de_mots_moyens, liste_de_mots_difficiles, start):
    nouveau_tour_de_jeu(nb_erreur, nb_erreur_max, mot_a_trouver, "")
    print("")
    print(message)
    print("Le mot recherché était :", afficher_le_mot(mot_a_trouver))
    print("temps de jeu :", round(time.time() - start, 2))
    print("")
    action = input("\"Entrée\" pour continuer ")
    return init_nouvelle_partie(liste_de_mots_faciles, liste_de_mots_moyens, liste_de_mots_difficiles)