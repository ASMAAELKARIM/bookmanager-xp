import pytest
from src.book import Book
from src.library import Library


@pytest.fixture
def bibliotheque():
    return Library()


@pytest.fixture
def petit_prince():
    return Book("Le Petit Prince", "Antoine de Saint-Exupery", "9782070612758")


def test_rechercher_un_livre_existant(bibliotheque, petit_prince):
    bibliotheque.ajouter_livre(petit_prince)

    assert bibliotheque.rechercher_par_titre("Le Petit Prince") == [petit_prince]


def test_rechercher_un_livre_inexistant(bibliotheque, petit_prince):
    bibliotheque.ajouter_livre(petit_prince)

    assert bibliotheque.rechercher_par_titre("Harry Potter") == []


def test_rechercher_parmi_plusieurs_livres(bibliotheque, petit_prince):
    etranger = Book("L'Etranger", "Albert Camus", "9782070360024")
    autre_edition = Book("Le Petit Prince", "Antoine de Saint-Exupery", "9782070408504")
    for livre in (petit_prince, etranger, autre_edition):
        bibliotheque.ajouter_livre(livre)

    resultats = bibliotheque.rechercher_par_titre("Le Petit Prince")

    assert resultats == [petit_prince, autre_edition]



def test_rechercher_par_auteur_existant(bibliotheque, petit_prince):
    bibliotheque.ajouter_livre(petit_prince)

    assert bibliotheque.rechercher_par_auteur("Antoine de Saint-Exupery") == [petit_prince]


def test_rechercher_par_auteur_inexistant(bibliotheque, petit_prince):
    bibliotheque.ajouter_livre(petit_prince)

    assert bibliotheque.rechercher_par_auteur("Victor Hugo") == []


def test_rechercher_par_auteur_plusieurs_livres(bibliotheque, petit_prince):
    etranger = Book("L'Etranger", "Albert Camus", "9782070360024")
    la_peste = Book("La Peste", "Albert Camus", "9782070360420")
    for livre in (petit_prince, etranger, la_peste):
        bibliotheque.ajouter_livre(livre)

    resultats = bibliotheque.rechercher_par_auteur("Albert Camus")

    assert resultats == [etranger, la_peste]