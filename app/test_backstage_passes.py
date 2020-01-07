from backstage_passes import Backstage_passes


def test_primer_caso():
    concierto = Backstage_passes("concierto", 10, 0)
    concierto.update_item()
    assert concierto.updated_item() == ("concierto", 9, 2)


def test_segundo_caso():
    concierto = Backstage_passes("concierto", 10, 0)
    for x in range(1, 11):
        concierto.update_item()
    assert concierto.updated_item() == ("concierto", 0, 12)


def test_tercer_caso():
    concierto = Backstage_passes("concierto", 10, 0)
    for x in range(1, 16):
        concierto.update_item()
    assert concierto.updated_item() == ("concierto", -5, 0)
