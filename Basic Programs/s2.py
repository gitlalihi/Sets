#Iterate over a set in Python
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set = set(user_input_list)

print("User's set:", user_set)

for i in user_set:
    print(i)