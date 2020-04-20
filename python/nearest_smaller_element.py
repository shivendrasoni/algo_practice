# https://www.interviewbit.com/problems/nearest-smaller-element/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):

        stack = []
        res = []
        i = 0
        while i < len(A):
            n = A[i]
            if not stack:
                res.append(-1)
                stack.append(n)
                i += 1
            else:
                if n > stack[-1]:
                    res.append(stack[-1])
                    stack.append(n)
                    i += 1
                else:
                    stack.pop()

        return res

if __name__ == '__main__':
    A = [1]
    print(Solution().prevSmaller(A))
