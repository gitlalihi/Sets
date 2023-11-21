#Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
def word_frequncy(word):
    word_set=set(word)
    word_counts={}
    for w in word_set:
        word_counts[w]=word.count(w)
    return word_counts
word=list(input("Enter your elements"))
print("Your frequency is :",word_frequncy(word))    