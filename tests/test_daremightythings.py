#!/usr/bin/env python

"""Tests for `daremightythings` package."""

import pytest
from daremightythings import interviews, robots


@pytest.fixture
def rover():
    """A pytest fixture for a planetary rover."""
    rover = robots.Rover(manufacturer="JPL")
    return rover


@pytest.mark.parametrize(
    "manufacturer, expected", [("JPL", True), ("The Empire", False)]
)
def test_landing(manufacturer, expected):
    """Sample pytest test function with the pytest rover fixture as an argument."""
    rover = robots.Rover(manufacturer=manufacturer)
    assert rover.land_on_mars() == expected
