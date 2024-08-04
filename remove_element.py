'''
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

* Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
  The remaining elements of nums are not important as well as the size of nums.
* Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val < 0 or val > 100:
            return 0

        if len(nums) >= 0 and len(nums) <= 100:
            k = 0
            j = len(nums) - 1

            while k <= j:
                if nums[k] != val:
                    k += 1
                else:
                    if nums[j] != val:
                        nums[k] = nums[j]
                    j -= 1      
            return k

        return 0
