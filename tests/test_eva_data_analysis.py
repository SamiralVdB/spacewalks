import pytest
from src.eva_data_analysis import text_to_duration, calculate_crew_size

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


def test_calculate_crew_size_for_no_crew():
    """
    Test that calculate_crew_size returns zero if there was no crew on board
    """
    actual_result = calculate_crew_size('')
    assert actual_result is None

@pytest.mark.parametrize("input_value, expected_result",[
    ('John Doe;', 1),
    ('John Doe;Eva Smit;Max Muster;', 3)
])
def test_calculate_crew_size(input_value:str, expected_result:int):
    """
    Test that calculate_crew_size returns the right number of crew members
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result

def test_calculate_crew_size_for_multiple_crew_members():
    """
    Test that calculate_crew_size returns zero if there was more than one crew member
    """
    actual_result = calculate_crew_size('John Doe;Eva Smit;Max Muster;')
    expected_result = 3
    assert actual_result == expected_result