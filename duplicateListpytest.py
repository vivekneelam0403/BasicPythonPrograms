
import sys
from duplicateList import getListDuplicates

def test_getListDuplicates(capsys):

    getListDuplicates([6,7,6,7,8,9])
    captured = capsys.readouterr()
    assert [6,7,6,7,8,9] in captured.out
    
    getListDuplicates([3,2,4,5,6])
    captured = capsys.readouterr()
    assert [3,2,4,5,6] in captured.out

    getListDuplicates([4,4,5,6,7])
    captured = capsys.readouterr()
    assert [4,4,5,6,7] in captured.out

    getListDuplicates([])
    captured = capsys.readouterr()
    assert [] in captured.out

    getListDuplicates([1])
    captured = capsys.readouterr()
    assert [1] in captured.out

    getListDuplicates([1,2])
    captured = capsys.readouterr()
    assert [1,2] in captured.out

    getListDuplicates([2,2])
    captured = capsys.readouterr()
    assert [2,2] in captured.out

'''
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
'''
