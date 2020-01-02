from normal_item import Normal_item


class Conjured(Normal_item):
    def update_quality(self):
        if self.sell_in > 0:
            self.quality - 2
            return self.quality
        else:
            self.quality - 2
            return self.quality
