from tests.settings import *


def test_item_example():
    item = Item("some item text", 6, 20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.sell_in == 5
    assert item.quality == 19


# here are some examples on how to use the
# xfail flags in settings.py:
# try them out to


def buggy_function():
    bug_fixed = False
    if bug_fixed:
        return 42
    else:
        return 43


@pytest.mark.xfail(
    xfail_bug_in_original,
    reason="42 bug: found in buggy_function, this should return 42!",
)
def test_bug_characterization():
    assert buggy_function() == 43


@pytest.mark.xfail(xfail_bug_fix, reason="42 bug: test for bug fix")
def test_bug_fixed():
    assert buggy_function() == 42


def new_feature():
    pass
    # return 'hello'


@pytest.mark.xfail(xfail_new_features, reason="new feature should return 'hello'")
def test_new_feature():
    assert new_feature() == "hello"
