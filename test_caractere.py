

def test_caractere(mot_a_trouver: set, lettre: str):
    lettre = lettre.lower()

    if len(lettre) > 1:
        return (mot_a_trouver, False, f"Le jeu demande une seule lettre et non '{lettre}'")
    
    for lettre_a_trouver in mot_a_trouver:
        if lettre_a_trouver["valeur"] == lettre:
            return (mot_a_trouver, False, f"Non ! \"{lettre}\" a déjà été choisie.")

    mot_a_trouver_nouveau = list(map(lambda lettre_a_touver: {"mystere": lettre_a_touver["mystere"], "MSA": lettre_a_touver["MSA"], "valeur": lettre_a_touver["mystere"]}
            if lettre_a_touver["MSA"] == lettre or lettre_a_touver["mystere"] == lettre_a_touver["valeur"] else
            {"mystere": lettre_a_touver["mystere"], "MSA": lettre_a_touver["MSA"], "valeur": "_"}, mot_a_trouver))

    if mot_a_trouver_nouveau == mot_a_trouver:
        return (mot_a_trouver, True, f"Non ! \"{lettre}\" ne fait pas parti de ce mot.")
    else:
        return (mot_a_trouver_nouveau, False, "")