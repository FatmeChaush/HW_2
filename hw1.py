def sum_of_min_and_max(arr):
    return min(arr) + max(arr) #

print(sum_of_min_and_max([1, 2, 3, 4, 5, 6, 8, 9]))
print(sum_of_min_and_max([-10, 5, 10, 100]))
print(sum_of_min_and_max([1]))

#В обобщение, кодът намира минималните и максималните стойности в дадения списък arr, 
#използвайки съответно функциите min() и max(). 
#След това изчислява сумата от тези две стойности и връща резултата.