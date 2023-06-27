from tests.settings import *

@pytest.fixture
def sulfuras():
    return Item("Sulfuras, Hand of Ragnaros", 5, 80)

@pytest.fixture
def gilded_rose(sulfuras):
    return GildedRose([sulfuras])

def test_sulfuras_quality_does_not_degrade(sulfuras, gilded_rose):
    gilded_rose.update_quality()
    assert sulfuras.quality == 80

def test_sulfuras_sell_in_doesnt_decrement(sulfuras, gilded_rose):
    sell_in_before = sulfuras.sell_in
    gilded_rose.update_quality()
    assert sulfuras.sell_in == sell_in_before

@pytest.mark.xfail(xfail_bug_in_original, reason="The quality should alway be 80")
def test_sulfuras_quality_not_always_80_bug(sulfuras, gilded_rose):
    sulfuras.quality = 50
    gilded_rose.update_quality()
    assert sulfuras.quality == 50

@pytest.mark.xfail(xfail_bug_fix, reason="The quality should alway be 80")
def test_sulfuras_quality_not_always_80_bug_fix(sulfuras, gilded_rose):
    sulfuras.quality = 50
    gilded_rose.update_quality()
    assert sulfuras.quality == 80
