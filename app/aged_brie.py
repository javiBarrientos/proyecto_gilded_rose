from gilded_rose import Normal_item


class Aged_brie(Normal_item):
    def update_quality(self, update_quality, set_sell_in):
        i = 0
        while i < self.set_sell_in:
            return self.update_quality + 1
        else:
            return self.update_quality + 2
