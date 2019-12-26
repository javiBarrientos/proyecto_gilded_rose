class Backstage_passes(Normal_item):
    def update_quality(self, quality, sell_in):
        if sell_in < 10 and sell_in > 5:
            quality + 2
            return quality
        if sell_in < 5 and sell_in > 0:
            quality + 3
            return quality
        else:
            quality = 0
            return quality
