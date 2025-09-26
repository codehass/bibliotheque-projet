from data import livres, utilisateurs
import math


def sort_books(books_list: list, param: str) -> list:
    return sorted(books_list, key=lambda livre: livre[param])


annee_de_publication = sort_books(livres, "année")


# Get the oldest book
plus_encien = min(annee_de_publication, key=lambda livre: livre["année"])
# annee_de_publication[0]

# Get the newest book
plus_recent = annee_de_publication[-1]


# count books
def count_livre(aime_livres):
    dict_count = {}
    for book_tuple in aime_livres:
        _, title = book_tuple
        if title in dict_count:
            dict_count[title] += 1
        else:
            dict_count[title] = 1
    return dict_count


def pagination(users_list, user_per_page=2):
    total_users = len(users_list)
    num_of_pages = int(math.ceil(total_users / user_per_page))
    print("num of pages", num_of_pages)

    current_page = 1
    index = 0
    while current_page <= num_of_pages:
        print(f"-------Page {current_page}----------")
        for index in range(index, user_per_page + index):
            if index < total_users:
                _, first_name, last_name, _ = users_list[index]
                print(f"    - {first_name}, {last_name}")
            else:
                break
            index += 1
        current_page += 1
        print("------------------------")

        if current_page <= total_users:
            input("\nPress Enter to view the next page...")
