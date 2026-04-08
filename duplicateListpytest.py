import pytest
from duplicateList import getListDuplicates

test_getListDuplicates = [
    ([6,7,6,7,8,9], [6,7]),
    ([3,2,4,5,6], []),
    ([4,4,5,6,7], [4]),
    ([],[]),
    ([1], []),
    ([1,2], []),
    ([2,2], [2])
]

@pytest.mark.parametrize("string1, expected", test_getListDuplicates)
def test_is_reverseString(string1, expected):
    assert getListDuplicates(string1) == expected

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__]) 