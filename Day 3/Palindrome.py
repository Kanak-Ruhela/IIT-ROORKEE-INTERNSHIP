n=int(input('Enter the number:-'))
rev=0
original=n
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
if original==rev: 
    print("Palindrome")
else:
    print("Not palindrome")
