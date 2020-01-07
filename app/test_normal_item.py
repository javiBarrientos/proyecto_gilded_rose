from normal_item import Normal_item


def test_primer_caso():
    maleta = Normal_item("maleta", 10, 0)
    maleta.update_item()
    assert maleta.updated_item() == ("maleta", 9, 0)
