

import jeu
import test_caractere

liste_de_mots_faciles, liste_de_mots_moyens, liste_de_mots_difficiles = jeu.init()
action = input("\"Entrée\" pour lancer le jeu ")
nb_erreur, start, nb_erreur_max, mot_a_trouver = jeu.init_nouvelle_partie(liste_de_mots_faciles, liste_de_mots_moyens, liste_de_mots_difficiles)
action = ""
message = ""
erreur = False

while action.lower() != "quit":
    if action != "":
        mot_a_trouver, erreur, message = test_caractere.test_caractere(mot_a_trouver, action)
        if erreur == True:
            nb_erreur += 1
        else:
            if jeu.test_victoire(mot_a_trouver):
                nb_erreur, start, nb_erreur_max, mot_a_trouver = jeu.fin_jeu(nb_erreur,
                                                                             nb_erreur_max,
                                                                             mot_a_trouver,
                                                                             "VICTOIRE",
                                                                             liste_de_mots_faciles,
                                                                             liste_de_mots_moyens,
                                                                             liste_de_mots_difficiles,
                                                                             start)
    
    if nb_erreur > nb_erreur_max:
        nb_erreur, start, nb_erreur_max, mot_a_trouver = jeu.fin_jeu(nb_erreur - 1,
                                                                     nb_erreur_max,
                                                                     mot_a_trouver,
                                                                     "PERDU : FIN DU JEU",
                                                                     liste_de_mots_faciles,
                                                                     liste_de_mots_moyens,
                                                                     liste_de_mots_difficiles,
                                                                     start)
    
    jeu.nouveau_tour_de_jeu(nb_erreur, nb_erreur_max, mot_a_trouver, message)
    action = input("Entrée une lettre (\"quit\" pour sortir du jeu) ")