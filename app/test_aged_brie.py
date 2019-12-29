from aged_brie import Aged_brie


def test_primer_caso():
    assert Aged_brie.update_quality(0, 10) == Aged_brie.update_quality(10, 0)
    assert Aged_brie.update_quality(
        20, -5) == Aged_brie.update_quality(40, -10)
