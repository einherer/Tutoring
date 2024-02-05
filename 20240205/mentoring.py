### PROBLEM STATEMENT
'''
Given a list of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,11,15,7], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# function with 'nums' as list and 'target' as integer
# the function returns a list
def index_calc(nums: list, target: int) -> list:
    
    # raising an error, when we don't get the correct type.
    #bool_ok = True
    #try:
    #     assert type(nums) == list
    #     assert type(target) == int
    #except:
    #    bool_ok = False
    
     # we need 2 indexes at the end, so we take the first 1 
     # and loop over ALL indexes in 'nums'
    #if bool_ok:
    
    if type(nums)!=list or type(target)!=int:
        return None
    
    for num1 in range(len(nums)):
    # for the second index we only check the indexes up to the 
    # first 1, as we don't want do check the sames indexes
        for num2 in range(num1):
        # add the 2 values and check if they match the target
            if nums[num1] + nums[num2] == target:
            # if so, rerutn the list
                return [num2, num1]        
# if no pair was found "nothing" will be return, so we get 'none'
    return []


print(index_calc(nums = [2,11,15,7], target = 9))
print(index_calc(nums = 46, target = 9))
