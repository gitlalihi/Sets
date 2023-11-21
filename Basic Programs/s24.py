#Python: Create set difference
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
original_set = set(user_input_list)
print("User's set:", original_set)

user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
other_set = set(user_input_list)
print("User's set:", other_set)

result1 = original_set.difference(other_set)
print("\nDifference of setc1 - setc2:"+result1)


result2= other_set.difference(original_set)
print("\nDifference of setc2 - setc1:"+result2)
