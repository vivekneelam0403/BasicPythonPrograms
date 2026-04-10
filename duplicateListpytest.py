
import sys
import pytest
from duplicateList import getListDuplicates

data_getListDuplicates = [
    ([6,7,6,7,8,9], "6\n7"),
    ([3,2,4,5,6], ""),
    ([4,4,5,6,7], "4"),
    ([],""),
    ([1], ""),
    ([1,2], ""),
    ([2,2], "2")
]

@pytest.mark.parametrize("input, expected_output", data_getListDuplicates)
def test_getListDuplicates(capsys, input, expected_output):
    getListDuplicates(input)
    captured = capsys.readouterr()
    assert expected_output in captured.out

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__]) 

