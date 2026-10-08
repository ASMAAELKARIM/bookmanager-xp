class User:
    """Représente un adhérent de la bibliothèque."""

    def __init__(self, nom: str, prenom: str, cin: str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.cin = cin