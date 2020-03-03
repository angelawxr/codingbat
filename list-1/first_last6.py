def first_last6(nums):
    """
    Given an array of ints, return True if 6 appears
    as either the first or last element in the array.
    The array will be length 1 or more.
    """
    return nums[0] == 6 or nums[-1] == 6


# print(first_last6([1, 2, 6]))
# print(first_last6([6, 1, 2, 3]))
# print(first_last6([13, 6, 1, 2, 3]))


def same_first_last(nums):
    """
    Given an array of ints, return True if the array is
    length 1 or more, and the first element and the 
    last element are equal.
    """
    return len(nums) > 0 and nums[0] == nums[-1]

print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))


def make_pi():
  """
  Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
  """
  pass

print(make_pi())

def common_end(a, b):
    """
    Given 2 arrays of ints, a and b, return True if 
    they have the same first element or they have the 
    same last element. Both arrays will be length 1 or more.
    """
    pass

print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))

