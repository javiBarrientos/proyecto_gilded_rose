from normal_item import Normal_item


class Sulfuras(Normal_item):
    def set_sell_in(self):
        assert self.sell_in == 0
        return self.sell_in

    def update_quality(self):
        assert self.update_quality == 80
        return self.quality
