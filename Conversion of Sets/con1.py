#Python program to convert Set into Tuple and Tuple into Set
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set = set(user_input_list)
print("User's set:", user_set)

print("Converted tuple is :",tuple(user_set))



userinput=input("Enter your strings seperated by a comma:").split(',')
user_tuple=tuple (item for item in userinput)
user_set=set(user_tuple)

print("Your set conversion is :",user_set)




