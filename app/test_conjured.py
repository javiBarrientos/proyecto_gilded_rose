from conjured import Conjured


def test_primer_caso():
    varita = Conjured("varita", 10, 10)
    varita.update_item()
    assert varita.updated_item() == ("varita", 9, 8)


def test_segundo_caso():
    varita = Conjured("varita", 10, 10)
    for day in range(1, 11):
        varita.update_item()
    assert varita.updated_item() == ("varita", 0, 0)


def test_tercer_caso():
    sombrero = Conjured("sombrero", 25, 30)
    for day in range(1, 31):
        sombrero.update_item()
    assert sombrero.updated_item() == ("sombrero", -5, 0)
