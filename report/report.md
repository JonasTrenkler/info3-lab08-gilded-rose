---
title: Lab 08 - Gilded Rose Kata
author: [Aaron Rau, Jonas Trenkler]
date: 2023-06-26
lang: 'en-US'
keywords: [TDD, Refactoring, Legacy Code, Kata]
---

# Lab 08 - Gilded Rose Kata

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


