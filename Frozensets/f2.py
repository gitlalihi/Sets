#Python program that converts a "frozen set" to a regular set and vice versa. Compare the differences between these two data types
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
frozen_set = frozenset(user_input_list)
print("User's frozenset:", frozen_set)
    
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set= set(user_input_list)
print("User's set:", user_set)

converted_to_frozenset = frozenset(user_set)

print("Frozen Set:", frozen_set)
print("Type of Frozen Set:", type(frozen_set))
print("\nRegular Set:", user_set)
print("Type of Regular Set:", type(user_set))
print("\nConverted to Frozen Set:", converted_to_frozenset)
print("Type of Converted Frozen Set:", type(converted_to_frozenset))
