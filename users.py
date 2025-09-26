from data import utilisateurs
#.1
majeurs = list(filter(lambda u: u[3] >= 18, utilisateurs))
print(utilisateurs)
print(majeurs)
