#Python | Maximum and Minimum in a Set
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set = set(user_input_list)

print("User's set:", user_set)
print("Maximum in a set is " ,max(user_set))
print("Minimum in a set is " ,min(user_set))