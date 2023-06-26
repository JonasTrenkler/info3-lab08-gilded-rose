from tests.settings import *

# create tests for normal items here...


# @pytest.mark.xfail(xfail_bug_fix, reason = "fixed value")
# def test_normal_quality_is_never_over_50_from_49_at_sell_in():
#    item = Item("normal with any name", 0, 51)
#    GildedRose([item]).update_quality()
#    assert item.sell_in == -1
#    assert item.quality == 48


@pytest.mark.xfail(xfail_bug_in_original, reason="bug in original")
def test_now():
    item = Item("normal with any name", 5, 60)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 59


@pytest.mark.xfail(xfail_bug_fix, reason="fixed value")
def test_goal():
    item = Item("normal with any name", 5, 60)
    GildedRose([item]).update_quality()
    assert item.sell_in == 4
    assert item.quality == 49
