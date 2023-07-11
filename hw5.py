def contains_digit(num, digit):
    while num > 0:
        if num%10 == digit:
            return True
        num//=10 
    return False

print(contains_digit(123, 4))
print(contains_digit(42, 2))
print(contains_digit(1000, 0))
print(contains_digit(12346789, 5))



