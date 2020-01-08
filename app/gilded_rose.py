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
        for item in self.items:
            self.update_quality()

    def inventario(self):
        traje_destreza = Normal_item()
        queso = Aged_brie()
        pocion_mongoose = Normal_item()
        sulfuro = Sulfuras()
        sulfuro_1 = Sulfuras()
        pase_rock = Backstage_passes()
        pase_kpop = Backstage_passes()
        pase_ozuna = Backstage_passes()
        pastel_mana = Conjured()