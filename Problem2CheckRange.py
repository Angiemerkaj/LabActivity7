#!bin/usr/bin/env
#Enxhi Merkaj 11/07/2023

#Create a function
def isNumberInRange(number, my_range):
    if number in my_range:
        return f"{number} is in the range {my_range}"
    else:
        return f"{number} is not in the range {my_range}"

my_range = range(1, 10)
#Prompt users to input a number
number_to_check = int(input("Enter a number: "))

result = isNumberInRange(number_to_check, my_range)
print(result)
