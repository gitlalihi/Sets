#Python Set | Pairs of complete strings in two sets
user_input = input("Enter elements separated by spaces: ")
user_input_list = user_input.split(",")  
user_set = set(user_input_list)
print("User's set:", user_set)

user_input2 = input("Enter elements separated by spaces: ")
user_input_list2 = user_input2.split(",")  
user_set2 = set(user_input_list2)
print("User's set:", user_set2)


def complete_strings(user_set,user_set2):
    com_strings=[]
    for str1 in user_set:
        for str2 in user_set2:
            if str1.endswith(str2) or str2.endswith(str1):
                com_strings.append((str1,str2))
    return com_strings

print(" Your complete string is :",complete_strings(user_set,user_set2))
