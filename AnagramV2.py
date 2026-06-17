import sys
import unittest

def replaceCharInWord(c, word2, word2length):
    index = 0
    while (index < word2length):
        if (c == (word2[index])):
            word2 = word2.replace(c,'',1)
            return word2,True
        index += 1
    return False
    


def isAnagram(word1, word2):
    word1length = len(word1)
    word2length = len(word2)

    if word1length != word2length:
        return False

    strindex1 = 0
    strindex2 = 0

    while (strindex1 < word1length):
        if replaceCharInWord(word1[strindex1], word2, word2length) == True:
            strindex1 += 1
            strindex2 = 0 
            word2length = len(word2)
        else: 
            if strindex2 > word2length:
                return False
            else: 
                strindex1 += 1
    return True
    

word1 = str(input("Enter first word: "))
word2 = str(input("Enter second word: "))

isAnagram(word1, word2)

if isAnagram(word1, word2) == True:
    print("anagram")
else: 
    print("not anagram")