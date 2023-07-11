def sum_of_divisorse(num):  
    result = 0             
    for i in range(1,num+1): 
        if (num %i == 0):   
                              
            result = result + i 

    return result

print(sum_of_divisorse(8))
print(sum_of_divisorse(7))
print(sum_of_divisorse(1))
print(sum_of_divisorse(1000))


