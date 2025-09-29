from data import utilisateurs, aime_livres
#.1
majeurs = list(filter(lambda u: u[3] >= 18, utilisateurs))
print(utilisateurs)
print("List majeurs :", majeurs)
#.2
noms_majuscules = list(map(lambda u: (u[1] + " " + u[2]).upper(), utilisateurs))
print("List majuscules :", noms_majuscules)
#.3
dict_amie_livres = {}
for utilisateur in utilisateurs:
    id, prenom, nom, age = utilisateur
    dict_amie_livres[prenom + " " + nom] = []
    for aime in aime_livres:
        if aime[0] == id:
            dict_amie_livres[prenom + " " + nom].append(aime[1])

print("Dictionnaire amis-livres :", dict_amie_livres)
    