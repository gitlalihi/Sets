#Python program to check if two frozensets are disjoint (set has no elements in common with other).
def check_disjoint(frozenset_1, frozenset_2):
    return frozenset_1.isdisjoint(frozenset_2)

def main():
    frozenset_1 = frozenset([1, 2, 3, 4, 5])
    frozenset_2 = frozenset([6, 7, 8])
    print("Original frozensets:")
    print(frozenset_1)
    print(frozenset_2)
    disjoint_result1 = check_disjoint(frozenset_1, frozenset_2)  
    if disjoint_result1:
        print("The frozensets are disjoint.")
    else:
        print("The frozensets are not disjoint.")    

if __name__ == "__main__":
    main()