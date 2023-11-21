#Convert Set to String in Python
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set = set(user_input_list)
print("User's set:", user_set)
S = ', '.join(user_set)
print("The datatype of s : " + str(type(S)))
print("Contents of s : ", S)