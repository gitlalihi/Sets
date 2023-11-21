#Python program that uses frozensets.
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
original_set = frozenset(user_input_list)
print("User's set:", original_set)

user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
other_set = frozenset(user_input_list)
print("User's set:", other_set)

print(original_set.isdisjoint(other_set))
print(original_set.difference(other_set))
print(original_set.union(other_set))
