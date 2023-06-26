from tests.settings import *

@pytest.fixture
def backstage_pass():
    return Item("Backstage passes to a TAFKAL80ETC concert", 666, 1)

@pytest.fixture
def gilded_rose(backstage_pass):
    return GildedRose([backstage_pass])

def test_backstage_pass_increases_quality_by_1_over_10_days_sell_in(backstage_pass, gilded_rose):
    quality_before = backstage_pass.quality
    gilded_rose.update_quality()
    assert backstage_pass.sell_in > 10
    assert backstage_pass.quality == quality_before + 1

def test_backstage_pass_increases_quality_by_2_at_10(backstage_pass, gilded_rose):
    backstage_pass.sell_in = 10
    quality_before = backstage_pass.quality
    gilded_rose.update_quality()
    assert backstage_pass.quality == quality_before + 2

def test_backstage_pass_increases_quality_by_2_at_6(backstage_pass, gilded_rose):
    backstage_pass.sell_in = 6
    quality_before = backstage_pass.quality
    gilded_rose.update_quality()
    assert backstage_pass.quality == quality_before + 2

def test_backstage_pass_increases_quality_by_3_at_5(backstage_pass, gilded_rose):
    backstage_pass.sell_in = 5
    quality_before = backstage_pass.quality
    gilded_rose.update_quality()
    assert backstage_pass.quality == quality_before + 3

def test_backstage_pass_increases_quality_by_3_at_1(backstage_pass, gilded_rose):
    backstage_pass.sell_in = 1
    quality_before = backstage_pass.quality
    gilded_rose.update_quality()
    assert backstage_pass.quality == quality_before + 3

def test_backstage_pass_quality_drops_to_zero(backstage_pass, gilded_rose):
    backstage_pass.sell_in = 0
    quality_before = backstage_pass.quality
    gilded_rose.update_quality()
    assert backstage_pass.quality == 0
