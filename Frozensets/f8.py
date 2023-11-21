#Python program that uses a frozenset as a key in a dictionary to create a hashable composite key for more complex data structures.
def main():
  user_dict = {}
  for i in range(3):
    key = input("Enter a key: ")
    value = input("Enter the value for {}: ".format(key))
    user_dict[key] = value
  print("User Input Dictionary:", user_dict)
  data = {frozenset(user_dict.items()): user_dict}
  for key, value in user_dict.items():
        print("Key:", key)
        print("Value:", value)
        print()

if __name__ == "__main__":
    main()

