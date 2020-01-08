from item import Item
from normal_item import Normal_item
from aged_brie import Aged_brie
from backstage_passes import Backstage_passes
from sulfuras import Sulfuras
from conjured import Conjured


class Gilded_rose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.inventario:
            self.update_quality()

    def inventario(self):
        traje_destreza = Normal_item("traje_destreza", 10, 20)
        queso = Aged_brie("aged_brie", 2, 0)
        pocion_mongoose = Normal_item("pocion_mongoose", 5, 7)
        mano_de_ragnaros = Sulfuras("mano_de_ragnarores", 0, 80)
        mano_de_ragnarores_1 = Sulfuras("mano_de_ragnarores", -1, 80)
        pase_rock = Backstage_passes("pase_rock", 15, 20)
        pase_kpop = Backstage_passes("pase_rock", 10, 49)
        pase_ozuna = Backstage_passes("pase_rock", 5, 49)
        pastel_mana = Conjured("patel_mana", 3, 6)

        lista_inventario = [traje_destreza, queso, pocion_mongoose,
                            mano_de_ragnaros, mano_de_ragnarores_1, pase_rock,
                            pase_kpop, pase_ozuna, pastel_mana]

        return lista_inventario
