from tests.settings import *

# create tests for normal items here...


def test_something():
    item = Item("name item", 5, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 4
    assert item.quality == 19
