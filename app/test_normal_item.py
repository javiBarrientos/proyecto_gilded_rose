from normal_item import Normal_item


def test_primer_caso():
    maleta = Normal_item("maleta", 10, 0)
    maleta.update_item()
    assert maleta.updated_item() == ("maleta", 9, 0)


def test_segundo_caso():
    regla = Normal_item("regla", 5, 20)
    regla.update_item()
    assert regla.updated_item() == ("regla", 4, 19)


def test_tercer_caso():
    taza = Normal_item("taza", 10, 10)
    for x in range(1, 21):
        taza.update_item()
    assert taza.updated_item() == ("taza", -10, 0)
