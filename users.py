from data import utilisateurs
#.1
majeurs = list(filter(lambda u: u[3] >= 18, utilisateurs))
print(utilisateurs)
print(majeurs)
#.2
noms_majuscules = list(map(lambda u: (u[1] + " " + u[2]).upper(), utilisateurs))
print(noms_majuscules)