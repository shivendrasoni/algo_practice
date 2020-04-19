# https://www.interviewbit.com/problems/maximum-unsorted-subarray/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):

        # Create another array B, which is A sorted.
        B = sorted([x for x in A])
        s = len(A)
        e = 0
        for i in range(len(A)-1, -1, -1):

            if B[i] != A[i]:
                s = min(s, i)
                e = max (e, i)

        if e-s >=0:
            return [s,e]
        else:
            return [-1]
