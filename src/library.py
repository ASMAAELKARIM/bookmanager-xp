from src.book import Book


class Library:
    """Catalogue des livres de la bibliothèque."""

    def __init__(self) -> None:
        self.livres: list[Book] = []

    def ajouter_livre(self, livre: Book) -> None:
        """Ajoute un livre au catalogue."""
        self.livres.append(livre)

    def rechercher_par_titre(self, titre: str) -> list[Book]:
        """Renvoie tous les livres dont le titre correspond."""
        return [livre for livre in self.livres if livre.titre == titre]