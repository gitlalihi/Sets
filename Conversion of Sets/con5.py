#Python | Convert a set into dictionary
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set = set(user_input_list)
print("User's set:", user_set)

res = dict.fromkeys(user_set, 0)
print ("final list", res)
print (type(res))