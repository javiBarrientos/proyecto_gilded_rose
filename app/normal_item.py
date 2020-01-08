from item import Item
from updatable import Updatable


class Normal_item(Item, Updatable):
    def __init__(self, name, sell_in, quality):
        self.name = name
        assert isinstance(name, str)
        self.sell_in = sell_in
        assert isinstance(sell_in, int)
        self.quality = quality
        assert isinstance(quality, int)

    def update_sell_in(self):
        self.sell_in -= 1
        return self.sell_in

    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2
        return self.quality

    def check_quality(self):
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50

    def update_item(self):
        Normal_item.update_sell_in(self)
        Normal_item.update_quality(self)
        Normal_item.check_quality(self)

    def updated_item(self):
        return self.name, self.sell_in, self.quality
