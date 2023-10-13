

import jeu
import test_caractere
import score

liste_de_mots_faciles, liste_de_mots_moyens, liste_de_mots_difficiles = jeu.init()
nom = input("Quel est ton nom ? ")

nb_parties_gagnees, nb_parties_jouees = score.lire_score(nom)

nb_erreur, start, nb_erreur_max, mot_a_trouver = jeu.init_nouvelle_partie(liste_de_mots_faciles, liste_de_mots_moyens, liste_de_mots_difficiles)
action = ""
message = ""
indice = 0

while action.lower() != "quit":
    if action != "":
        mot_a_trouver, erreur, message = test_caractere.test_caractere(mot_a_trouver, action)
        if erreur == True:
            nb_erreur += 1
            indice += 1
            if indice == 2:
                indice = 0
                indice_txt = ""
                for lettre in mot_a_trouver:
                    if lettre["valeur"] == "_":
                        indice_txt = lettre["MSA"]
                message += " / indice : " + indice_txt
        else:
            indice == 0
            if jeu.test_victoire(mot_a_trouver):
                nb_erreur, start, nb_erreur_max, mot_a_trouver = jeu.fin_jeu(nb_erreur,
                                                                             nb_erreur_max,
                                                                             mot_a_trouver,
                                                                             "VICTOIRE",
                                                                             liste_de_mots_faciles,
                                                                             liste_de_mots_moyens,
                                                                             liste_de_mots_difficiles,
                                                                             start,
                                                                             nom)
    
    if nb_erreur > nb_erreur_max:
        nb_erreur, start, nb_erreur_max, mot_a_trouver = jeu.fin_jeu(nb_erreur - 1,
                                                                     nb_erreur_max,
                                                                     mot_a_trouver,
                                                                     "PERDU : FIN DU JEU",
                                                                     liste_de_mots_faciles,
                                                                     liste_de_mots_moyens,
                                                                     liste_de_mots_difficiles,
                                                                     start,
                                                                     nom)
        message = ""
    
    jeu.nouveau_tour_de_jeu(nb_erreur, nb_erreur_max, mot_a_trouver, message)
    action = input("Entrée une lettre (\"quit\" pour sortir du jeu) ")