# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        a = 0
        b = 0
        res = []
        while a < len(A) and b < len(B):
            if A[a] < B[b]:
                res.append(A[a])
                a += 1
            else:
                res.append(B[b])
                b += 1
        while a < len(A):
            res.append(A[a])
            a += 1
        while b < len(B):
            res.append(B[b])
            b += 1

        for i in range(len(res)):
            val = str(res[i])
            if i < len(A):
                A[i] = val
            else:
                A.append(val)

        # print(' '.join(A) + ' ')

if __name__ == '__main__':
    s = Solution()
    A = [-4, 3]
    s.merge(A, [-2, -2])
    print(A)
    # print(s.merge([-4, 3], [-2, -2]))

