import sqlite3
import matplotlib.pyplot as plt


def requete(req):
    """Exécute une requete sur la bdd etab_sco.sqlite

    retourne la liste des résultats
    """

    # Ouverture de la connexion
    bdd = sqlite3.connect('etab_sco.sqlite')
    cur = bdd.cursor()

    # Traitement de la requête
    cur.execute(req)
    liste_res = cur.fetchall()

    # Fermeture de la connexion
    cur.close()
    bdd.close()

    return liste_res
