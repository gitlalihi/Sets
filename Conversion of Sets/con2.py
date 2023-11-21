#Python | Convert set into a list
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set = set(user_input_list)
print("User's set:", user_set)
s = list(user_set)
print(type(s))