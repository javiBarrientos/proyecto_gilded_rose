from normal_item import Normal_item


class Sulfuras(Normal_item):
    def __init__(self, name, sell_in, quality):
        self.name = name
        assert isinstance(name, str)
        self.sell_in = sell_in
        assert isinstance(sell_in, int)
        self.quality = quality
        assert isinstance(quality, int)

    def update_sell_in(self):
        pass

    def update_quality(self):
        pass

    def update_item(self):
        Sulfuras.update_sell_in(self)
        Sulfuras.update_quality(self)
