from aged_brie import Aged_brie


def test_primer_caso():
    bollicao = Aged_brie("bollicao", 10, 50)
    bollicao.update_quality()
    bollicao.set_quality(80)
