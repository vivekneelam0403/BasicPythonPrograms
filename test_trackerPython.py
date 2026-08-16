import pytest
from tracker import calculate_status

data_calculate_status = [
    (85, "pass"),
    (43, "fail"),
    (60, "pass")
]

@pytest.mark.parametrize("input, expected_output", data_calculate_status)
def test_calculate_status(input, expected_output):
    result = calculate_status(input)
    assert result == expected_output


if __name__ == "__main__":
    pytest.main([__file__])