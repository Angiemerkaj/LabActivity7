#!bin/usr/bin/env
#Enxhi Merkaj 11/07/2023

#Create a function
def multiplyList(numbers):
    result = 1
    for num in numbers:
        result *= num #multiply the numbers
    return result

my_list = [5, 2, 7, -1]
result = multiplyList(my_list)
print("The result of multiplying all the numbers in the list is:", result)
