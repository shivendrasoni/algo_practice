# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, arr):

        # -INF assumed to be -9999999
        # current_max
        current_max = -9999999
        max_val = -9999999

        # Iterate over each element in arr
        for n in arr:

            # if the sum of current_max and n (current number) > current_number
            if current_max+n > n:
                current_max = current_max + n

            else:
                current_max = n

            # if current_max is more than global_max, update global_max
            if current_max > max_val:
                max_val = max

        return max_val
