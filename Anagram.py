import sys
import unittest


def isAnagram(word1, word2):
    word1length = len(word1)
    word2length = len(word2)

    if word1length != word2length:
        return False

    strindex1 = 0
    strindex2 = 0 

    while (strindex1 < word1length):
        if (word1[strindex1]).lower() == (word2[strindex1]).lower():
            word2 = word2.replace(word1[strindex1],'',1)
            strindex1 += 1
            strindex2 = 0 
            word2length = len(word2)
        else: 
            if strindex2 < word2length:
                strindex2 += 1
            else:
                return False
    return True
    


class TestMyFunctions(unittest.TestCase):

    def test_is_anagram(self):
        result = isAnagram("race","care")
        self.assertEqual(result, True)

    def test_is_not_anagram(self):
        result = isAnagram("carc","race")
        self.assertEqual(result, False)

    def test_different_lengths(self):
        result = isAnagram("car","race")
        self.assertEqual(result, False)
    
    def test_empty_strings(self):
        result = isAnagram("","")
        self.assertEqual(result, True)

    def test_multiple_same_char(self):
        result = isAnagram("caat", "acct")
        self.assertEqual(result, False)

    def test_uppercase_letter(self):
        result = isAnagram("cAre", "RAce")
        self.assertEqual(result, True)

    

if __name__ == '__main__':
    unittest.main()

word1 = str(input("Enter first word: "))
word2 = str(input("Enter second word: "))

isAnagram(word1, word2)