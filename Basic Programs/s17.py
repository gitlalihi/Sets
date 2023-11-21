#Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.
def remove_duplicates(strings):
    seen = set()
    result = []
    for string in strings:
        if string not in seen:
            seen.add(string)
            result.append(string)
    return result

strings = input("Enter your strings separated by a comma:").split(',')
print("Original list of strings:", strings)
print("List of strings after removing duplicates:")
print(remove_duplicates(strings))