#Python program that performs common set operations like union, intersection, and difference of two frozensets.
def main():
    user_input = input("Enter elements separated by spaces: ")
    user_input_list = user_input.split()  
    frozenset_x = frozenset(user_input_list)
    print("User's frozenset:", frozenset_x)
    
    user_input = input("Enter elements separated by spaces: ")
    user_input_list = user_input.split()  
    frozenset_y= frozenset(user_input_list)
    print("User's frozenset:", frozenset_y)
    
    
    union_result = frozenset_x.union(frozenset_y)
    print("Union of two said frozensets:", union_result)
    
    intersection_result = frozenset_x.intersection(frozenset_y)
    print("Intersection of two said frozensets:", intersection_result)
    
    difference_result1 = frozenset_x.difference(frozenset_y)
    
    difference_result2 = frozenset_y.difference(frozenset_x)
    print("Difference of (frozenset_x - frozenset_y)", difference_result1)
    print("Difference of (frozenset_y - frozenset_x)", difference_result2)

if __name__ == "__main__":
    main()