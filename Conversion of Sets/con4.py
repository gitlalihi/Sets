#Convert String to Set in Python
string = input("Enter your String:")
print("The datatype of string : " + str(type(string)))
print("Contents of string : " + string)

string = {*string}
print("\nAfter the conversion")
print("The datatype of string : " + str(type(string)))
print("Contents of string : ", string)