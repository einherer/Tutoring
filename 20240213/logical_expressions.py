a = 12
b = 43
c = 74
d = 65

# Logical expression:
# > greater
# < lower
# == equal
# >= greater or equal
# <= lower or equal
# and / or
# not

print(a, b, c, d)
print(a > b)
print(a < b)
print(not (a > b))
print(not (a < b))

def min(nums):
    helper = nums[0]

    for num in nums:
        if num < helper:
            helper = num

    return helper



def max(nums):
    helper = nums[0]

    for num in nums:
        if num > helper:
            helper = num

    return helper

print(min([a, b, c, d]))
print(max([a, b, c, d]))

if a < b and b < c:
    print("b is between and c")

if a > b or b < c:
    print("either a is bigher than b or b is smaller than c or both")

if b > d or c < d:
    print("either a is bigher than b or b is smaller than c or both")
else:
    print("here we are")