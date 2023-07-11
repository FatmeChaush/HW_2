def biggest_difference(arr):
    min = arr[0]    
    max = arr[0]    

    for num in arr: 
        if num < min:  
           min = num   

        if num > max:
            max = num
        
    return max - min   

print(biggest_difference([1, 2, 3, 4, 5]))


