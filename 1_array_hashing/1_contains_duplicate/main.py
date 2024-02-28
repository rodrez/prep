from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print("func:%r took: %2.4f sec" % (f.__name__, te - ts))
        return result

    return wrap


# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# Constraints:
#
#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109


# With python the first attempt would be to convert a list to set and then
# compare the length
@timing
def first(nums):
    return len(set(nums)) != len(nums)


# In a language where casting an arry to a set doesn't work we could use a
# hashmap.
@timing
def second(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > 1:
            return True

    return False


# We could go the super simple route and do a straight for loop
# Works great when there are duplicates but it's terribly slow
# when there aren't any duplicates
@timing
def third(nums):
    for i, num in enumerate(nums):
        if num in nums[i + 1 :]:
            return True
    return False


# with recursion
# works well for smaller data sets, terrible for bigger data sets
@timing
def fourth(nums, index=0):
    # If the index is greater than the length of the array the all elements
    # should be unique
    if index == len(nums):
        return False

    current_element = nums[index]
    # We already verified the previous index, so we only verify forward
    rest_arr = nums[index + 1 :]

    # The current element is in the array so there are duplicates
    if current_element in rest_arr:
        return True

    # No duplicates on this round, let's increase the index and go to next round
    return fourth(nums, index + 1)


# Run the test
print(
    first([i for i in range(100000)])
)  # Should be True, because it contains duplicates
print(
    second([i for i in range(100000)])
)  # Should be True, because it contains duplicates
print(
    third([i for i in range(100000)])
)  # Should be True, because it contains duplicates
print(
    # fourth([i for i in range(10)])
    fourth([i for i in range(100000)])
)  # Should be True, because it contains duplicates

# print("TRUES")
# print(first([1, 2, 3, 4]))  # Should be True, because it contains duplicates
# print(second([1, 2, 3, 4]))  # Should be True, because it contains duplicates
# print(third([1, 2, 3, 4]))  # Should be True, because it contains duplicates
# print(fourth([1, 2, 3, 4]))  # Should be True, because it contains duplicates
