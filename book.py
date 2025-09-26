from data import livres, aime_livres


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
