from gilded_rose import Normal_item


class Aged_brie(Normal_item):
    def update_quality(update_quality, set_sell_in):
        while i < set_sell_in:
            update_quality = update_quality + 1
            set_sell_in = set_sell_in - 1
        else:
            update_quality = update_quality + 2
            set_sell_in = set_sell_in - 1

        return update_quality
        return set_sell_in
