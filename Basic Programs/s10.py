#Python program to count number of vowels using sets in given string
def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
result = count_vowels(input_string)
print(f"Number of vowels in the given string: {result}")