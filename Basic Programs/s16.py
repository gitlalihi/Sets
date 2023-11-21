#Python Set | Check whether a given string is Heterogram or not
def is_heterogram(s):
   s = s.lower()
   unique_letters = set()
   for char in s:
        if char.isalpha() and char in unique_letters:
                return False
        else:
                unique_letters.add(char)
        return True


input_string = input("Enter your string/sentence")
result = is_heterogram(input_string)
if result:
    print(f"{input_string} is a heterogram.")
else:
    print(f"{input_string} is not a heterogram.")