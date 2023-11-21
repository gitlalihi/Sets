# Python program to create a shallow copy of sets.
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
original_set = set(user_input_list)
print("User's set:", original_set)

user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
other_set = set(user_input_list)
print("User's set:", other_set)

result=original_set.copy()
print("Your shallow copy is :"+ result)