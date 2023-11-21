#Find the size of a Set in Python
import sys
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
user_set = set(user_input_list)

print("User's set:", user_set)
print("The size of the set  :"+ str(sys.getsizeof(user_set))+"bytes")