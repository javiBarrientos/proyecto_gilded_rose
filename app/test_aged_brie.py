from aged_brie import *


def test_primer_caso():
    brownie = Aged_brie("brownie", 10, 0)
    brownie.update_quality()
    brownie.set_quality(80)
