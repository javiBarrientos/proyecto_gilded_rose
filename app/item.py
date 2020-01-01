class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def get_name(self):
        return self.name

    def get_sell_in(self):
        return self.sell_in

    def get_quality(self):
        return self.quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
