from aged_brie import Aged_brie


def test_primer_caso():
    assert Aged_brie.update_quality(0, 10) == Aged_brie.update_quality(10, 0)


def test_dias_negativos():
    assert Aged_brie.update_quality(51, 30) == False
