from typing import List

class Solution:
    """
    Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:
    Given nums = [1,1,1,2,2,3],
    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
    It doesn't matter what you leave beyond the returned length.
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_same_nums = 0
        curr_num = nums[0]
        index = 0
        while index < len(nums):
            if nums[index] == curr_num:
                if num_same_nums + 1 > 2:
                    nums.pop(index)
                else:
                    num_same_nums += 1
                    index += 1
            else:
                curr_num = nums[index]
                num_same_nums = 1
                index += 1
        return len(nums)

Solution().removeDuplicates([0,0,1,1,1,1,2,3,3])