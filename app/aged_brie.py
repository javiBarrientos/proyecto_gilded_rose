from item import Normal_item


class Aged_brie(Normal_item):
    def update_quality(self, update_quality, sell_in):
        if self.sell_in >= 0:
            return update_quality + 1
        else:
            return update_quality + 2


if __name__ == "__main__":
