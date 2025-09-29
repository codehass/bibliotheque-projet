from users import *
from data import *
def afficher_recapitulatif():
    print("=== Récapitulatif de la bibliothèque ===")
    print(f"Nombre total de livres : {len(livres)}")
    print(f"Nombre total d'utilisateurs : {len(utilisateurs)}")
    print("\nListe des livres :")
    for livre in livres:
        print(f"- {livre}")
    print("\nListe des utilisateurs :")
    for utilisateur in utilisateurs:
        print(f"- {utilisateur}")

afficher_recapitulatif()