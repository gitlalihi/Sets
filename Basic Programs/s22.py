#Python program to check if a given set is a superset of itself and a superset of another given set.
def check_superset(original_set, other_set):
   is_superset_of_itself = original_set.issuperset(original_set)
   is_superset_of_other = original_set.issuperset(other_set)
   return is_superset_of_itself, is_superset_of_other


user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
original_set = set(user_input_list)
print("User's set:", original_set)

user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split()  
other_set = set(user_input_list)
print("User's set:", other_set)

is_superset_itself, is_superset_other = check_superset(original_set, other_set)

print(f"Original set: {original_set}")
print(f"Other set: {other_set}")
print(f"Is the original set a superset of itself? {is_superset_itself}")
print(f"Is the original set a superset of the other set? {is_superset_other}")