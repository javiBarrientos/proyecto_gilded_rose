from normal_item import Normal_item


class Backstage_passes(Normal_item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        assert isinstance(name, str)
        self.sell_in = sell_in
        assert isinstance(sell_in, int)
        self.quality = quality
        assert isinstance(quality, int)

    def update_quality(self):
        if self.sell_in <= 10 and self.sell_in > 5:
            self.quality += 2
            return self.quality
        if self.sell_in < 5 and self.sell_in > 0:
            self.quality += 3
            return self.quality
        else:
            self.quality = 0
            return self.quality

    def update_item(self):
        Backstage_passes.update_quality(self)
        Normal_item.update_sell_in(self)
        Normal_item.check_quality(self)
