class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            if nums[idx] > target:
                continue

            for idx2 in range(idx + 1, len(nums)):
                if nums[idx] + nums[idx2] == target:
                    return [ idx, idx2 ]

            return None

obj = Solution()

print(obj.twoSum([2, 7, 11, 15], 9))