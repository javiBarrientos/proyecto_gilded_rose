from conjured import Conjured


def test_primer_caso():
    fetiche_sonrriente = Conjured("fetiche_sonrriente", 10, 0)
    fetiche_sonrriente.update_quality()
    fetiche_sonrriente.set_quality(9)
