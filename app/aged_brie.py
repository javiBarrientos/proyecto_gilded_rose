class Aged_brie(Normal_item):
    def update_quality(self, update_quality, set_sell_in):
        if set_sell_in >= 0:
            return update_quality + 1
        else:
            return update_quality + 2
