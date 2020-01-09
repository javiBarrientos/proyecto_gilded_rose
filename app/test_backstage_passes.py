from backstage_passes import Backstage_passes


def test_primer_caso():
    concierto = Backstage_passes("concierto", 10, 0)
    concierto.update_item()
    assert concierto.updated_item() == ("concierto", 9, 2)


def test_segundo_caso():
    concierto = Backstage_passes("concierto", 15, 7)
    for day in range(1, 13):
        concierto.update_item()
    assert concierto.updated_item() == ("concierto", 3, 3)


def test_tercer_caso():
    concierto = Backstage_passes("concierto", 10, 0)
    for day in range(1, 16):
        concierto.update_item()
    assert concierto.updated_item() == ("concierto", -5, 0)
