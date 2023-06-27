from tests.settings import *

@pytest.fixture
def item():
    return Item("random normal item", 5, 20)

@pytest.fixture
def gilded_rose(item):
    return GildedRose([item])

def test_quality_decreases_by_one(item, gilded_rose):
    gilded_rose.update_quality()
    assert item.quality == 19

def test_sell_in_decreses_by_one(item, gilded_rose):
    gilded_rose.update_quality()
    assert item.sell_in == 4

def test_sell_in_negative(item, gilded_rose):
    item.sell_in = 0
    gilded_rose.update_quality()
    assert item.sell_in == -1

def test_quality_not_negative(item, gilded_rose):
    item.quality = 0
    gilded_rose.update_quality()
    assert item.quality == 0

def test_quality_expiration_starts_at_0(item, gilded_rose):
    item.sell_in = 1
    gilded_rose.update_quality()
    assert item.quality == 19

def test_quality_degradation_doubles_after_expiration(item, gilded_rose):
    item.sell_in = 0
    gilded_rose.update_quality()
    assert item.quality == 18

@pytest.mark.xfail(xfail_bug_in_original, reason="Item quality should never be negative")
def test_quality_not_negative_starts_negative_bug(item, gilded_rose):
    item.quality = -1
    gilded_rose.update_quality()
    assert item.quality == -1

@pytest.mark.xfail(xfail_bug_fix, reason="Item quality should never be negative")
def test_quality_not_negative_starts_negative_bug_fix(item, gilded_rose):
    item.quality = -1
    gilded_rose.update_quality()
    assert item.quality == 0

@pytest.mark.xfail(xfail_bug_in_original, reason="Item quality should not be instantiated over 50")
def test_quality_starts_over_50_bug(item, gilded_rose):
    item.quality = 666
    assert item.quality == 666
    gilded_rose.update_quality()
    assert item.quality == 665

@pytest.mark.xfail(xfail_bug_fix, reason="Item quality should not be instantiated over 50")
def test_quality_starts_over_50_bug_fix(item, gilded_rose):
    item.quality = 666
    assert item.quality == 50
    gilded_rose.update_quality()
    assert item.quality == 49
