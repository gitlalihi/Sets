#Python set to check if string is pangram
#A pangram is a sentence that contains every letter of the alphabet at least once.

def is_pangram(input_string):
    
    input_string = input_string.lower()
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    return set(input_string) >= alphabet_set

input_str = input("Enter your sentence")
if is_pangram(input_str):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
