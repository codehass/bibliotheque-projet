from data import livres, aime_livres


def sort_books(books_list: list, param: str) -> list:
    return sorted(books_list, key=lambda livre: livre[param])


annee_de_publication = sort_books(livres, "année")
