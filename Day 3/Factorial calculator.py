def factorial_iterative(n):
    fact=1
    for i in range (1,n+1):
        fact = fact*i
    return fact
print(factorial_iterative(int(input('enter the number:-'))))
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(int(input('enter the number:-'))))
   
