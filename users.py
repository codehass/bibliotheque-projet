from data import utilisateurs
#.1
majeurs = list(filter(lambda u: u[3] >= 18, utilisateurs))
print(utilisateurs)
print(majeurs)
#.2
noms_majuscules = list(map(lambda u: (u[1] + " " + u[2]).upper(), utilisateurs))
print(noms_majuscules)
#.3
for u in utilisateurs:
    nom_complet = f"{u[1].upper()} {u[2].upper()} ({u[3]} ans)"
    livres = ", ".join([f"'{livre}'" for livre in u[2]])
    print(f"{nom_complet} aime : {livres}")