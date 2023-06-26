---
title: Lab 08 - Gilded Rose Kata
author: [Aaron Rau, Jonas Trenkler]
date: 2023-06-26
lang: 'en-US'
keywords: [TDD, Refactoring, Legacy Code, Kata]
---

# Lab 08 - Gilded Rose Kata

Group: Aaron Rau, Jonas Trenkler  
Repository: <https://github.com/JonasTrenkler/info3-lab08-gilded-rose>

## Characterization Tests

`Characterization Tests` is an approach to work with legacy code, coined by Michael Feathers in 'Working Effectively with Legacy Code' (FEATHERS 2004: p. 186).
There is also a short summary with an example online on his [website](https://michaelfeathers.silvrback.com/characterization-testing).

Writing these tests is more of a process to determine what a piece of code does.
The relevant part is not what the specifications say that the software *should* do, but what the implementation actually *does* do.
Characterization Tests help to preserve this behavior and allow conscious changes to it, instead of breaking things as side-effect.

In the book Feathers provides a step by step description to this process: 

    1. Use a piece of code in a test harness.
    2. Write an assertion that you know will fail.
    3. Let the failure tell you what the behavior is.
    4. Change the test so that it expects the behavior that the code produces.
    5. Repeat.

An important point is to rename the test to something useful in step four.
This gives context to the test, whether the behavior is intended or a bug.
Naming the test is also a way to verbalize what the programmer learned about the codes functionality.
It will also help to identify regression if it breaks later on.
Using the `xfail` functionality of `pytest` helps to distinguish bugs, see [xfail](https://docs.pytest.org/en/7.3.x/how-to/skipping.html#skip-all-test-functions-of-a-class-or-module)

As described in the lab, we used the `testloop` bash-script to continuously run pytest, while writing the tests.

Instead of the `UnitTest` approach to test fixtures, using a `setup` function, we used the `pytest`-native `@fixture` keyword: https://docs.pytest.org/en/7.3.x/explanation/fixtures.html#about-fixtures.
The test fixtures look like this:

```python
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

```

After writing some tests for normal items and the aged brie we tested out the code coverage tool.
Even though only one special item was tested, there were only 7 untested lines of code.
Martin Fowler stresses, that the code coverage alone is not an indicator of the quality of the tests.

```console
╰─ pytest --cov-report term-missing --cov gilded_rose/refactored tests
================================= test session starts =================================platform linux -- Python 3.11.3, pytest-7.3.2, pluggy-1.0.0
rootdir: /home/jonas/Studium/B15_Info3/labs/info3-lab08-gilded-rose
plugins: cov-4.1.0
collected 16 items                                                                    

tests/test_aged_brie.py ....                                                    [ 25%]
tests/test_normal.py ....Xx                                                     [ 62%]
tests/examples/example_test.py Xx                                               [ 75%]
tests/examples/gilded_rose_example_test.py .Xxx                                 [100%]

---------- coverage: platform linux, python 3.11.3-final-0 -----------
Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
gilded_rose/refactored/gilded_rose.py      36      7    81%   21-26, 36
---------------------------------------------------------------------
TOTAL                                      36      7    81%

```

After adding the test cases for Sulfuras and the Backstage passes, the code coverage went up to 100%:

```console
╰─ pytest --cov-report term-missing --cov gilded_rose/refactored tests --ignore=tests/examples/
============================================================================= test session starts ==============================================================================platform linux -- Python 3.11.3, pytest-7.3.2, pluggy-1.0.0
rootdir: /home/jonas/Studium/B15_Info3/labs/info3-lab08-gilded-rose
plugins: cov-4.1.0
collected 21 items                                                                                                                                                             

tests/test_aged_brie.py ....                                                                                                                                             [ 19%]
tests/test_backstage_ticket.py ......                                                                                                                                    [ 47%]
tests/test_normal.py ......Xx                                                                                                                                            [ 85%]
tests/test_sulfuras.py ..x                                                                                                                                               [100%]

---------- coverage: platform linux, python 3.11.3-final-0 -----------
Name                                    Stmts   Miss  Cover   Missing
---------------------------------------------------------------------
gilded_rose/refactored/gilded_rose.py      36      0   100%
---------------------------------------------------------------------
TOTAL                                      36      0   100%


=================================================================== 18 passed, 2 xfailed, 1 xpassed in 0.07s ===================================================================
```


