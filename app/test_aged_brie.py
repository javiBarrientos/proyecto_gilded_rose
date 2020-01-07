from aged_brie import Aged_brie


def test_primer_caso():
    pato = Aged_brie("pato", 10, 0)
    pato.update_item()
    assert pato.updated_item() == ("pato", 9, 0)
