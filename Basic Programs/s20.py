#Python program to find all the anagrams in a given list of strings and then group them together.
def group_anagrams(strings):
    anagram_groups = {}
    for word in strings:
        key = frozenset(word)
        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]

    return list(anagram_groups.values())
input_strings = ["listen", "silent", "enlist", "hello", "world", "python", "typhon"]
result = group_anagrams(input_strings)

print("List of strings:")
print(input_strings)
print("\nAnagram groups:")
print(result)