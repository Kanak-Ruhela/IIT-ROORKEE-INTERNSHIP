def safe_divide_simple(numerator, denominator):
    if denominator == 0:
        return 0 
    return numerator / denominator
print(safe_divide_simple(12, 3)) 
print(safe_divide_simple(12, 0))  
