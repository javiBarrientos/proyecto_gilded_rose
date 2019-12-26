class Aged_brie(Normal_item):
    def update_quality(quality, sell_in):
        if sell_in >= 0:
            return quality + 1
        else:
            return quality + 2


if __name__ == "__main__":
