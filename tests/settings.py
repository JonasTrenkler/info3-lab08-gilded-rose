import pytest

# this file contains all imports
# and xfail flags for all tests.
# this is the only file you need to import in your tests.

# use this to switch between the original and your refactored version.

# from gilded_rose.gilded_rose import GildedRose, Item

from gilded_rose.refactored.gilded_rose import GildedRose, Item

# XFAIL FLAGS
# use this to be able to refactor without the need to pertaining found
# bugs.

# initial xfail setting:
# xfail everything
xfail_bug_in_original = False
xfail_bug_fix = True
xfail_new_features = True


# xfail setting during refactoring and bug fixing
# xfail everything!

# xfail_bug_in_original = True
# xfail_bug_fix = True
# xfail_new_features = True

# xfail setting after fixing bugs
# xfail_bug_fix should really fail now!

# xfail_bug_in_original = True
# xfail_bug_fix = False
# xfail_new_features = True


# after implementing the new feature:

# xfail_new_features = False
