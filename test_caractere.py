

def test_caractere(mot_a_trouver: set, lettre: str):
    if len(lettre) > 1:
        return (mot_a_trouver, False, f"Le jeu demande une seule lettre et non '{lettre}'")
    
    mot_a_trouver_nouveau = list(map(lambda lettre_a_touver: {"mystere": lettre_a_touver["mystere"], "valeur": lettre_a_touver["mystere"]}
            if lettre_a_touver["mystere"] == lettre or lettre_a_touver["mystere"] == lettre_a_touver["valeur"] else
            {"mystere": lettre_a_touver["mystere"], "valeur": "_"}, mot_a_trouver))

    if mot_a_trouver_nouveau == mot_a_trouver:
        return (mot_a_trouver, True, f"Non ! {lettre} ne fait pas parti de ce mot.")
    else:
        return (mot_a_trouver_nouveau, False, "")