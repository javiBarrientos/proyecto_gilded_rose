from gilded_rose import Normal_item


class Aged_brie(Normal_item):
    def update_quality(quality, sell_in):
        while quality < 50:
            if quality > 50:
                quality += 0
                sell_in -= 1
                if sell_in < 0:
                    quality += 2
                    sell_in -= 1
            else:
                quality += 1
                sell_in -= 1

        return quality, sell_in
