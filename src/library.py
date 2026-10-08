from src.book import Book
from src.user import User


class Library:
    """Catalogue des livres et des adhérents de la bibliothèque."""

    def __init__(self) -> None:
        self.livres: list[Book] = []
        self.utilisateurs: list[User] = []

    def ajouter_livre(self, livre: Book) -> None:
        """Ajoute un livre au catalogue."""
        self.livres.append(livre)

    def rechercher_par_titre(self, titre: str) -> list[Book]:
        """Renvoie tous les livres dont le titre correspond."""
        return [livre for livre in self.livres if livre.titre == titre]

    def rechercher_par_auteur(self, auteur: str) -> list[Book]:
        """Renvoie tous les livres de l'auteur donné."""
        return [livre for livre in self.livres if livre.auteur == auteur]

    def ajouter_utilisateur(self, utilisateur: User) -> None:
        """Enregistre un adhérent."""
        self.utilisateurs.append(utilisateur)

    def emprunter(self, cin: str, isbn: str) -> None:
        """Emprunte un livre si toutes les règles du client sont respectées."""
        self._trouver_utilisateur(cin)
        livre = self._trouver_livre(isbn)
        if not livre.disponible:
            raise ValueError("Livre indisponible")
        livre.disponible = False

    def _trouver_utilisateur(self, cin: str) -> User:
        """Renvoie l'adhérent ayant ce CIN, sinon refuse."""
        for utilisateur in self.utilisateurs:
            if utilisateur.cin == cin:
                return utilisateur
        raise ValueError("Utilisateur inexistant")

    def _trouver_livre(self, isbn: str) -> Book:
        """Renvoie le livre ayant cet ISBN, sinon refuse."""
        for livre in self.livres:
            if livre.isbn == isbn:
                return livre
        raise ValueError("Livre inexistant")