#Python program to accept the strings which contains all the vowels
def contains_all_vowels(s):
    s_lower = s.lower()
    vowels = set('aeiou')
    return vowels.issubset(set(s_lower))

# Example usage
input_string = input("Enter a string: ")

if contains_all_vowels(input_string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")
