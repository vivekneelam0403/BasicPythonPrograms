import pytest
from printListElements import traversingListFunction

# Pytest 

test_traversingListFunction = [
    ([1,3,4,5,6], [1,6,3,5,4]),
    ([1,3,3,3,4], [1,4,3,3,3]),
    ([7,7,7], [7,7,7]),
    ([], []),
    ([1,3,4,5,], [1,5,3,4]),
    ([1], [1]),
    ([1,3], [1,3]),
]

@pytest.mark.parametrize("string1, expected", test_traversingListFunction)
def test_is_reverseString(string1, expected):
    assert traversingListFunction(string1) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])

#__________________________________________________________________________________