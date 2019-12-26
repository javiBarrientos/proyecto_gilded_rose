class Aged_brie(Normal_item):
    def __init__(self, update_quality, sell_in):
        self.update_quality = update_quality
        self.sell_in = sell_in

    def update_quality(update_quality, sell_in):
        if sell_in >= 0:
            return update_quality + 1
        else:
            return update_quality + 2


if __name__ == "__main__":
