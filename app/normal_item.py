from item import Item


class Normal_item(Item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def set_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        else:
            self.quality -= 2


'''
    def set_quality(self, value):
        if self.quality + value > 50:
            self.quality = 50
            if self.quality + value >= 0:
                self.quality + value
            else:
                self.quality = 0
'''
