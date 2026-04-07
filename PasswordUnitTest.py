import pytest

def setIntegerKey(intkey):
    intkey=0

def setStringKey(strkey):
    strkey=""

def DigitalVault():
    print("tested")

def IsEvenPassword(int_user_input):
    isEvenPassword = int_user_input
    return isEvenPassword

def IsPrimePassword(int_user_input):
    isPrimePassword = int_user_input
    return isPrimePassword

def SumOfDigitsPassword(int_user_input):
    sumOfDigitsPassword = int_user_input
    return sumOfDigitsPassword

def ReverseStringPassword(int_user_input):
    reverseStringPassword = int_user_input
    return reverseStringPassword

def CountVowelsPassword(str_user_input):
    countVowelsPassword = str_user_input
    return countVowelsPassword

def IsPalindromePassword(str_user_input):
    isPalindromePassword = str_user_input
    return isPalindromePassword 


test_data_IsEvenPassword = [
    # Verify an even input password unlocks the vault when it matches the stored key
    (670, 1340)
    # Verify an odd input password does not unlock the vault
    (67, 1340)
    # Verify a incorrect input password does not unlock the vault
    (670, 1340)
]
    
test_data_IsPrimePassword = [
    # Verify an prime input password unlocks the vault when it matches the stored key
    (74, 67)
    # Verify an non-prime input password does not unlock the vault
    (74, 68)
    # Verify an incorrect input password does not unlock the vault 
    (6706700098788467, 67)
]

test_data_SumOfDigitsPassword = [
    # Verify the sum of the digits input password unlocks the vault when it matches the stored key
    (67, 13)
    # Verify the incorrect input password does not unlock the vault
    (67, 90)
]

test_data_ReverseStringPassword = [
    # Verify a reversed string input password unlocks the vault when it matches the stored key
    ("live", "evil")
    # Verify a incorrect string input password does not unlock the vault
    ("evil", "evil")
]

test_data_CountVowelsPassword = [
    # Verify that the correct amount of vowels unlocks the vault when it matches the stored key
    ("evil", "evil2")
    # Verify a wrong amount of string input password does not unlock the vault
    ("evl", "evil2")
]

test_data_IsPalindromePassword = [
    # Verify that the palindrome of the string unlocks the vault when it matches the stored key
    ("evilx", "live")
    # Verify the the non-palindrome of the string does not unlock the vault
    ("evil", "red40Cheetos")
]


@pytest.mark.parametrize("user_input, stored_key", test_data_IsEvenPassword)
def test_IsEvenPassword(user_input, stored_key):
    setIntegerKey(stored_key)
    assert IsEvenPassword(user_input) == stored_key

@pytest.mark.parametrize("int_user_input, stored_key", test_data_IsPrimePassword)
def test_IsPrimePassword(int_user_input, stored_key):
    setIntegerKey(stored_key)
    assert IsPrimePassword(int_user_input) == stored_key

@pytest.mark.parametrize("int_user_input, stored_key", test_data_SumOfDigitsPassword)
def test_SumOfDigitsPassword(int_user_input, stored_key):
    setIntegerKey(stored_key)
    assert SumOfDigitsPassword(int_user_input) == stored_key

@pytest.mark.parametrize("str_user_input, stored_key", test_data_ReverseStringPassword)
def test_ReverseStringPassword(str_user_input, stored_key):
    assert ReverseStringPassword(str_user_input) == stored_key

@pytest.mark.parametrize("str_user_input, stored_key", test_data_CountVowelsPassword)
def test_CountVowelsPassword(str_user_input, stored_key):
    assert CountVowelsPassword(str_user_input) == stored_key

@pytest.mark.parametrize("str_user_input, strored_key", test_data_IsPalindromePassword)
def test_IsPalindromPassword(str_user_input, strored_key):
    assert IsPalindromePassword(str_user_input) == strored_key

if __name__ == "__main__":
    print("Running pytest test cases...\n")
    pytest.main([__file__])
