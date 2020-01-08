from sulfuras import Sulfuras


def test_primer_caso():
    azufre = Sulfuras("azufre", 0, 80)
    azufre.update_item()
    assert azufre.updated_item() == ("azufre", 0, 80)


def test_segundo_caso():
    azufre = Sulfuras("azufre", 0, 80)
    for day in range(1, 40):
        azufre.update_item()
    assert azufre.updated_item() == ("azufre", 0, 80)
