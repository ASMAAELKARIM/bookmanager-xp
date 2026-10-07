class Book:
    """Représente un livre de la bibliothèque."""

    def __init__(self, titre: str, auteur: str, isbn: str) -> None:
        self.titre = self._valider_titre(titre)
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True

    @staticmethod
    def _valider_titre(titre: str) -> str:
        """Refuse un titre vide."""
        if not titre:
            raise ValueError("Le titre est obligatoire")
        return titre