from item import Item
from normal_item import Normal_item
from aged_brie import Aged_brie


def main():
    item1 = Aged_brie("Bollicao" 10, 0)
    print("day 0")
    for x in range(1, 31):
        print("day" + " " + str(x))
        item1.get_sell_in()
        item1.get_quality()
        item1.set_quality(20)
        print(item1)


main()
