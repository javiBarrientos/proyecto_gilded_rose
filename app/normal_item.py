from item import Item


class Normal_item(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2

    def check_quality(self):
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50
