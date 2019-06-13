import sqlite3
import matplotlib.pyplot as plt


# La fonction
def requete(req):
    """ exécute une requête sur la bdd location.sqlite
    retourne la liste des résultats
    """
    bdd = sqlite3.connect('locations.sqlite')
    cur = bdd.cursor()

    cur.execute(req)
    liste_res = cur.fetchall()

    cur.close()
    bdd.close()

    return liste_res


## Un exemple d'utilisation
# req = """ SELECT * FROM stations; """
# stations = requete(req)
# print(stations)

req = """SELECT code_postal, COUNT(*) AS nb FROM abonnés WHERE code_postal LIKE "69%" AND code_postal <= 69009 \
GROUP BY code_postal"""
arr = requete(req)

les_X = [arr[i][0] for i in range(len(arr))]
les_Y = [arr[i][1] for i in range(len(arr))]

plt.bar(les_X, les_Y, 0.5)
plt.title("Nombre d'abonnées par arrondissement")
plt.show()
