from normal_item import Normal_item


class Backstage_passes(Normal_item):
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
