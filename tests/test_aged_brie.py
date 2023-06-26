from tests.settings import *

@pytest.fixture
def aged_brie():
    return Item("Aged Brie", 5, 10)

@pytest.fixture
def gilded_rose(aged_brie):
    return GildedRose([aged_brie])

def test_aged_brie_quality_decrements(aged_brie, gilded_rose):
    gilded_rose.update_quality()
    assert aged_brie.quality == 11

def test_aged_brie_sell_in_decrements(aged_brie, gilded_rose):
    gilded_rose.update_quality()
    assert aged_brie.sell_in == 4

def test_aged_brie_sell_in_negative(aged_brie, gilded_rose):
    aged_brie.sell_in = 0
    gilded_rose.update_quality()
    assert aged_brie.sell_in == -1

def test_aged_brie_quality_inc_not_over_50(aged_brie, gilded_rose):
    aged_brie.quality = 50
    gilded_rose.update_quality()
    assert aged_brie.quality == 50
