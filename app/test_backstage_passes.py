from backstage_passes import Backstage_passes


def test_primer_caso():
    architects = Backstage_passes("architects", 10, 0)
    architects.update_quality()
    architects.set_quality(20)
