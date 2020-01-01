class Gilded_rose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        pass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def get_name(self):
        return self.name

    def get_sell_in(self):
        return self.sell_in

    def get_quality(self):
        return self.quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


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
