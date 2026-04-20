import sys 
import pytest
from detectiveProgram import detectiveProgram 

data_detectiveProgram = [
    (["hello077hello"], "077"),
    (["hellohihey"], ""),
    (["hello89fifty"], ""),
    (["hello4567"], "456\n567"),
    (["h670i673"], "670\n673"),
    (["h670673i"], "670\n706\n067\n673"),
    ([""], ""),
    (["56788"], "567\n678\n788")
    (["hellonocde678"], "678")
]

@pytest.mark.parametrize("input, expected_output", data_detectiveProgram)
def test_getListDuplicates(capsys, input, expected_output):
    detectiveProgram(input)
    captured = capsys.readouterr()
    assert expected_output in captured.out

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__]) 

    