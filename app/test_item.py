from item import Item


def test_primer_caso():
    estuche = Item('Estuche', 100, 10)
    assert estuche.get_name() == 'Estuche'
    assert estuche.get_sell_in() == 100
    assert estuche.get_quality() == 10
