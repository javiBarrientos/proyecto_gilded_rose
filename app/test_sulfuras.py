from sulfuras import Sulfuras


def test_primer_caso():
    azufre = Sulfuras("azufre", 0, 80)
    azufre.update_item()
    assert azufre.updated_item() == ("azufre", 0, 80)
