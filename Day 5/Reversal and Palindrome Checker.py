def check_palindrome(word):
    if word == word[::-1]:
        print("Yes, it is a palindrome!")
    else:
        print("No, it is not a palindrome.")
a=input('enter the word:-')
check_palindrome(a)
