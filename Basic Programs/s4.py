#Python | Remove items from Set
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set = set(user_input_list)

print("User's set:", user_set)

while user_set:
    user_set.discard(max(user_set))
print("Removed items from the set is :",user_set)    
