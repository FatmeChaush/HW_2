def is_prime(num): 
    if num == 1:     
        return False 


    for i in range(4, num):
        if num % i == 0: 
            return False 

    return True 

print(is_prime(1))
print(is_prime(2))
print(is_prime(8))
print(is_prime(11))
print(is_prime(-10))
