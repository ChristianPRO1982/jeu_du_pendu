import os

def ecrire_score(nom, nb_parties_gagnees, nb_parties_jouees):
    nom += '.txt'
    if not os.path.exists(nom):
        with open(nom, 'w') as file:
            file.write(nb_parties_gagnees)
            file.write(nb_parties_jouees)

def lire_score(nom):
    nom += '.txt'
    if os.path.exists(nom):
        with open(nom, 'r') as file:
            i = 0
            for line in file:
                i += 1
                if i == 1:
                    nb_parties_gagnees = int(line.strip())
                if i == 2:
                    nb_parties_jouees = int(line.strip())
    else:
        nb_parties_gagnees = 0
        nb_parties_jouees = 0

    return nb_parties_gagnees, nb_parties_jouees