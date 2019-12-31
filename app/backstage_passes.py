from gilded_rose import Normal_item


class Backstage_passes(Normal_item):
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.sell_in < 10 and self.sell_in > 5:
            self.quality + 2
            return self.quality
        if self.sell_in < 5 and self.sell_in > 0:
            self.quality + 3
            return self.quality
        else:
            self.quality = 0
            return self.quality
