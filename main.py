

import jeu
import test_caractere

liste_de_mots = jeu.init()
action = input("\"Entrée\" pour lancer le jeu ")
nb_erreur, start, mot_a_trouver = jeu.init_nouvelle_partie(liste_de_mots)
action = ""
message = ""
erreur = False

while action.lower() != "quit":
    if action != "":
        mot_a_trouver, erreur, message = test_caractere.test_caractere(mot_a_trouver, action)
        if erreur == True:
            nb_erreur += 1
    
    if nb_erreur > 6:
        print("PERDU : FIN DU JEU")
        print("Le mot rechercher était :", jeu.afficher_le_mot(mot_a_trouver))
        nb_erreur, start, mot_a_trouver = jeu.init_nouvelle_partie(liste_de_mots)
        action = input("\"Entrée\" pour continuer ")
        jeu.nouveau_tour_de_jeu(nb_erreur, mot_a_trouver, message)
    else:
        jeu.nouveau_tour_de_jeu(nb_erreur, mot_a_trouver, message)
    
    action = input("Entrée une lettre (\"quit\" pour sortir du jeu) ")