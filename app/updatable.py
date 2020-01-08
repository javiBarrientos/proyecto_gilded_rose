class Updatable():
    def __init__(self, name, sell_in, quality):
        self.name = name
        assert isinstance(name, str)
        self.sell_in = sell_in
        assert isinstance(sell_in, int)
        self.quality = quality
        assert isinstance(quality, int)

    def update_quality(self):
        pass
