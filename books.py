from data import livres
import math


def sort_books(books_list: list, param: str) -> list:
    return sorted(books_list, key=lambda livre: livre[param])


annee_de_publication = sort_books(livres, "année")


def display_list_of_books(books):
    for book in books:
        print(" ", book)
    print("\n")


# Obtenir le livre le plus ancien
plus_ancien = min(annee_de_publication, key=lambda livre: livre["année"])

# Obtenir le livre le plus récent
plus_recent = annee_de_publication[-1]


# Compter les livres aimés
def count_livre(aime_livres):
    dict_count = {}
    for _, title in aime_livres:
        if title in dict_count:
            dict_count[title] += 1
        else:
            dict_count[title] = 1
    return dict_count


def pagination(users_list, user_per_page=2):
    total_users = len(users_list)
    num_of_pages = math.ceil(total_users / user_per_page)
    print(f"Nombre de pages : {num_of_pages}\n")

    current_page = 1
    index = 0
    while current_page <= num_of_pages:
        print(f"------- Page {current_page} -------")
        for i in range(index, index + user_per_page):
            if i < total_users:
                _, first_name, last_name, _ = users_list[i]
                print(f"    - {first_name} {last_name}")
            else:
                break
        index += user_per_page
        current_page += 1
        print("------------------------------")

        if current_page <= num_of_pages:
            input("\nAppuyez sur Entrée pour voir la page suivante...")
