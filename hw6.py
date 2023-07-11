def contains_digits(num, digits): 
    for digit in digits:         
        if str(digit) not in str(num): 
            return False                 
        return True                       
    
print(contains_digits(402123, [0, 3, 4]))


