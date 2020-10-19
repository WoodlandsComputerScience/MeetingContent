favourite_numbers = [12,30,35,42,80]
#                     0, 1, 2, 3, 4
first_number = favourite_numbers[0] # 12
print(first_number)

favourite_numbers.append(34) # adding to the end of the list
favourite_numbers.pop(0) # removing element 0 of the list
favourite_numbers.remove(35) # removing value 35 of the list, only the first occurance
print(favourite_numbers) # [30,42,80,34]