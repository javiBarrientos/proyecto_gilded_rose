from normal_item import Normal_item


def test_primer_caso():
    maleta = Normal_item("maleta", 10, 0)
    maleta.update_quality()
    assert maleta.set_quality(0)
