#Concatenated string with uncommon characters in Python
def uncommon_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    uncommon_chars = (set1 - set2) | (set2 - set1)
    result = ''.join(uncommon_chars)
    return result


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = uncommon_characters(string1, string2)
print(f"Concatenated string with uncommon characters: {result}")
