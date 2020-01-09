from gilded_rose import Gilded_rose
from aged_brie import Aged_brie
from backstage_passes import Backstage_passes
from sulfuras import Sulfuras
from conjured import Conjured
from normal_item import Normal_item


def test_dia_0():
    lista_items = Gilded_rose([
        Normal_item("+ 5 Dexterity Vest", 10, 20),
        Aged_brie("Aged Brie", 2, 0),
        Normal_item("Elixir of the Mongoose", 5, 7),
        Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Conjured("Conjured Mana Cake", 3, 6)])
    lista_items.update_quality()
    lista_items.updated_items = lista_items = Gilded_rose([
        Normal_item("+ 5 Dexterity Vest", 9, 19),
        Aged_brie("Aged Brie", 1, 1),
        Normal_item("Elixir of the Mongoose", 4, 6),
        Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 14, 0),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 9, 50),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 4, 0),
        Conjured("Conjured Mana Cake", 2, 4)])
    assert lista_items() == updated_items()
