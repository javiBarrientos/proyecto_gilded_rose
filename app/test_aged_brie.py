from aged_brie import Aged_brie


def test_primer_caso():
    pato = Aged_brie("pato", 10, 0)
    pato.update_item()
    assert pato.updated_item() == ("pato", 9, 1)


def test_segundo_caso():
    queso = Aged_brie("queso", -10, 15)
    for day in range(1, 15):
        queso.update_item()
    assert queso.updated_item() == ("queso", -24, 43)


def test_tercer_caso():
    pato = Aged_brie("pato", 10, 0)
    for day in range(1, 31):
        pato.update_item()
    assert pato.updated_item() == ("pato", -20, 50)
