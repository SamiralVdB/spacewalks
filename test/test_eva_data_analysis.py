import pytest
from src.eva_data_analysis import text_to_duration

def test_text_to_duration_for_whole_hours():
    """
    Test that text_to_duration returns expected value for whole hours
    """
    assert text_to_duration("10:00") == 10

def test_text_to_duration_for_hour_fraction():
    """
        Test that text_to_duration returns expected value with only non-zero minute components
    """
    assert text_to_duration("00:30") == 0.5

def test_text_to_duration_for_whole_hour_and_fraction():
    """
        Test that text_to_duration returns expected value with whole hours and non-zero minute components
    """
    assert text_to_duration("10:20") == pytest.approx(10.33333333, abs = 1e-5)