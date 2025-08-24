from datetime import datetime
from pathlib import Path
import sys

# Ensure project root is on sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from tradingagents.dataflows.utils import get_next_weekday


def test_weekend_returns_following_monday():
    saturday = "2024-03-30"  # Saturday
    sunday = "2024-03-31"    # Sunday
    expected = datetime(2024, 4, 1)

    assert get_next_weekday(saturday) == expected
    assert get_next_weekday(sunday) == expected


def test_weekday_returns_same_date():
    weekday = "2024-04-02"  # Tuesday
    expected = datetime(2024, 4, 2)

    assert get_next_weekday(weekday) == expected
