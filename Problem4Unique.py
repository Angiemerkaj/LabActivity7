#!bin/usr/bin/env
#Enxhi Merkaj 11/07/2023

#Create function
def uniqueElements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1, 3, 3, 3, 6, 2, 3, 5]
result = uniqueElements(my_list)
print("Original list:", my_list)
print("List with unique elements:", result) #print unique list
