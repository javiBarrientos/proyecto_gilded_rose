from gilded_rose import Normal_item


class Aged_brie(Normal_item):
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(sell_in, quality):
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

        return sell_in, quality
