import pytest
from src.book import Book
from src.library import Library
from src.user import User

CIN = "AB123456"
ISBN = "9782070612758"


@pytest.fixture
def bibliotheque():
    return Library()


@pytest.fixture
def petit_prince():
    return Book("Le Petit Prince", "Antoine de Saint-Exupery", ISBN)


@pytest.fixture
def adherent():
    return User("ElKarim", "Asmaa", CIN)


def test_emprunt_accepte_utilisateur_existant_livre_disponible(bibliotheque, petit_prince, adherent):
    bibliotheque.ajouter_livre(petit_prince)
    bibliotheque.ajouter_utilisateur(adherent)

    bibliotheque.emprunter(CIN, ISBN)

    assert petit_prince.disponible is False


def test_emprunt_refuse_livre_indisponible(bibliotheque, petit_prince, adherent):
    petit_prince.disponible = False
    bibliotheque.ajouter_livre(petit_prince)
    bibliotheque.ajouter_utilisateur(adherent)

    with pytest.raises(ValueError):
        bibliotheque.emprunter(CIN, ISBN)


def test_emprunt_refuse_utilisateur_inexistant(bibliotheque, petit_prince):
    bibliotheque.ajouter_livre(petit_prince)

    with pytest.raises(ValueError):
        bibliotheque.emprunter(CIN, ISBN)
    assert petit_prince.disponible is True


def test_emprunt_refuse_livre_inexistant(bibliotheque, adherent):
    bibliotheque.ajouter_utilisateur(adherent)

    with pytest.raises(ValueError):
        bibliotheque.emprunter(CIN, ISBN)