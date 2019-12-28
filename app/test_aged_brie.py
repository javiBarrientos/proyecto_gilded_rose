from aged_brie import Aged_brie


def test_primer_caso():
    assert (10, 0) == Aged_brie.update_quality(0, 10)
