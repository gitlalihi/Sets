#Python program to create a symmetric difference.
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
original_set = set(user_input_list)
print("User's set:", original_set)

user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
other_set = set(user_input_list)
print("User's set:", other_set)

result1=original_set.symmetric_difference(other_set)
print("Your sysmetric differnce between two sets is :",result1)

result2=other_set.symmetric_difference(original_set)
print("Your sysmetric differnce between two sets is :",result2)