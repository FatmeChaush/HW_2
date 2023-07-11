def is_int_palindrome(num):
    if num == 1:
        return False
    

    num_str = str(num)

    return num_str == num_str[::-1]
       
    return True

    return False
print(is_int_palindrome(1))
print(is_int_palindrome(42))
print(is_int_palindrome(100001))
print(is_int_palindrome(999))
print(is_int_palindrome(123))

#Синтаксисът `s[::-1]` означава "обърнете низа `s`".
#Така че сравняваме оригиналния низ с обърнатия низ, за да видим дали са равни. 
#Ако са, тогава цялото число е палиндром.
