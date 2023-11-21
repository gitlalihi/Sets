#Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
def find_combinations_of_three(nums, target_val):
    nums = list(set(nums))
    result = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            complement = target_val - nums[i] - nums[j]
            if complement in nums[:i] + nums[j+1:]:
               result.add(tuple(sorted((nums[i], nums[j], complement))))
    return list(result)


nums = list(int(input("Enter your elements:")))
target_val = int(input("Enter your target value:"))
print("Original list of numbers:")
print(nums)
print("Target value:", target_val)
print("Combine three numbers whose sum equals the target number:")
print(find_combinations_of_three(nums, target_val))
