class Solution(object):
    def maxSubArray(self, nums):
        max_count = nums[0]
        result = 0

        for i in nums:
            if result < 0:
                result = 0

            result += i

            if result > max_count:
                max_count = result

        return max_count
