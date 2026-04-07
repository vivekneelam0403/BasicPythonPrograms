import pytest 
from characterCount import characterCountFunction

test_characterCountFunction = [
    ("banana", "a", 3 ),
    ("hi", "i", 1),
    ("alfredo", "n", 0),
    ("", "", 0),
    ("", "a", 0)
]

@pytest.mark.parametrize("string1, string2, expected", test_characterCountFunction)
def test_is_reverseString(string1, string2, expected):
    assert characterCountFunction(string1, string2) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__]) 