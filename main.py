from books import (
    pagination,
    annee_de_publication,
    display_list_of_books,
    plus_ancien,
    plus_recent,
    count_livre,
)
from data import utilisateurs, aime_livres


def menu():
    choices = [
        "1 - Trier les livres par année de publication",
        "2 - Identifier le livre le plus ancien et le plus récent",
        "3 - Afficher le dictionnaire des livres avec le nombre de 'j'aime'",
        "4 - Afficher les utilisateurs avec pagination",
        "5 - Quitter le programme",
    ]

    print("-------- Menu -------")
    print("---------------------")

    while True:
        for choice in choices:
            print(" ", choice)
        print("\n")

        try:
            choice = int(input("Entrez votre choix : "))
        except ValueError:
            print("Merci d'entrer une valeur valide !\n")
            continue

        if choice == 1:
            print("\nLivres triés par année de publication :")
            display_list_of_books(annee_de_publication)

        elif choice == 2:
            print("\nLivre le plus ancien et le plus récent :")
            print(" - Plus ancien :", plus_ancien)
            print(" - Plus récent :", plus_recent)
            print("\n")

        elif choice == 3:
            print("\nDictionnaire des livres avec le nombre de 'j'aime' :")
            print(count_livre(aime_livres))
            print("\n")

        elif choice == 4:
            pagination(utilisateurs, 2)
            print("\n")

        elif choice == 5:
            print("Programme terminé. Au revoir !")
            break

        else:
            print("Choix non valide, merci d'essayer à nouveau !\n")


menu()
