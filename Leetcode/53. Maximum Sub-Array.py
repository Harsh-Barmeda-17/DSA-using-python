# Apprach - 1

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


# Approach - 2 ( Kadane algorithm ) 

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = max_sum = num[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
