import pytest
from src.book import Book

TITRE = "Le Petit Prince"
AUTEUR = "Antoine de Saint-Exupery"
ISBN = "9782070612758"


@pytest.fixture
def livre():
    return Book(TITRE, AUTEUR, ISBN)


def test_creer_un_livre_avec_titre_auteur_isbn(livre):
    assert livre.titre == TITRE
    assert livre.auteur == AUTEUR
    assert livre.isbn == ISBN


def test_un_nouveau_livre_est_disponible_par_defaut(livre):
    assert livre.disponible is True


def test_creer_un_livre_sans_titre_est_refuse():
    with pytest.raises(ValueError):
        Book("", AUTEUR, ISBN)