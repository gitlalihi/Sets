#Python program to find the third largest number from a given list of numbers.Use the Python set data type.
def third_largest(nums):
    nums = set(nums)
    if len(nums) < 3:
        return None
    nums = list(nums)
    nums.sort(reverse=True)
    return nums[2]


nums =list(int(input(" Enter your list:")))
print("Original list of numbers:",nums)
print("Third largest number of the said list of numbers:", third_largest(nums))
