from item import Item


class Normal_item(Item):
    def set_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.quality > 0:
            self.set_quality(-1)
        else:
            self.set_quality(-2)
        self.set_sell_in()

    def set_quality(self, value):
        if self.quality + value > 50:
            self.quality = 50
            if self.quality + value >= 0:
                self.quality + value
            else:
                self.quality = 0
