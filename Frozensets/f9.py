# Python program that generates a frozenset containing the squares of all odd numbers from 1 to 15 using set comprehension.
def main():
    odd_numbers = {x**2 for x in range(1, 16) if x % 2 != 0}
    frozenset_of_squares = frozenset(odd_numbers)
    print("Frozenset of Squares of Odd Numbers:", frozenset_of_squares)

if __name__ == "__main__":
    main()