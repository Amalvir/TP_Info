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


req1 = "SELECT X FROM etab_sco"
req2 = "SELECT Y FROM etab_sco"

abscisses = requete(req1)
ordonnee = requete(req2)

les_x, les_y = [], []

print(type(abscisses[1][0]))
for i in range(len(abscisses)):

    if type(abscisses[i][0]) == float and type(ordonnee[i][0]) == float and ordonnee[i][0] <= 7200000 \
            and ordonnee[i][0] >= 6000000:
        les_x.append(abscisses[i][0])
        les_y.append(ordonnee[i][0])


plt.plot(les_x, les_y, 'b.')
plt.show()
