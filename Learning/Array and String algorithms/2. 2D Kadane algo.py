def kadane(nums):
    current_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

def kadane_2D(matrix):
    Rows = len(matrix)
    Cols = len(matrix[0])
    max_sum = float('-inf')

    for left in range(Cols):
        temp = [0] * Rows

        for right in range(left, Cols):
            for i in range(Rows):
                temp[i] += matrix[i][right]

            max_sum = max(max_sum, kadane(temp))

    return max_sum
