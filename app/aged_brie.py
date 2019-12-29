from gilded_rose import Normal_item


class Aged_brie(Normal_item):
    def update_quality(update_quality, set_sell_in):
        while update_quality < 50:
            if update_quality > 50:
                update_quality += 0
                set_sell_in -= 1
                if set_sell_in < 0:
                    update_quality += 2
                    set_sell_in -= 1
            else:
                update_quality += 1
                set_sell_in -= 1

        return update_quality, set_sell_in

    print(update_quality(0, 10))
