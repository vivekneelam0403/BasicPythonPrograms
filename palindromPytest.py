import pytest
from palindrome import isPalindromeFunction


test_isPalindromeFunction = [
    ("racecar", True),
    ("", True),
    ("hello", False),
    ("racecars", False),
    ("a", True),
]




@pytest.mark.parametrize("string1, expected", test_isPalindromeFunction)
def test_is_reverseString(string1, expected):
    assert isPalindromeFunction(string1) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])