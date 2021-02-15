import pytest

@pytest.mark.parametrize("number1, expected", [(65, "Normal"), (50, "Borderline Low"), (20, "Low"),])


def test_blood_test_combined(number1, expected):
    from blood_test import analyze_HDL
    answer = analyze_HDL(number1)
    assert answer == expected
