from normal_item import Normal_item


class Sulfuras(Normal_item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_sell_in(self):
        assert self.sell_in == 0
        return self.sell_in

    def update_quality(self):
        assert self.quality == 80
        return self.quality

    def update_item(self):
        Sulfuras.update_sell_in(self)
        Sulfuras.update_quality(self)
