def check_anagram(word1, word2):
    if sorted(word1)==sorted(word2):
        print("word is anagrom")
    else:
        print("word is not anagram")
a= input("enter the first letter:-")
b=input("enter the second letter:-")
check_anagram(a,b)
