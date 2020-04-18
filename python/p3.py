# https://www.interviewbit.com/problems/valid-number/

class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        res = 1
        dec = 0
        exp = 0
        arr = A.split('e')
        if len(arr) > 2 or len(arr[0])==0 or len(arr[-1]) == 0:
            return 0
        elif len(arr) == 2:
            exp = len(arr[0])

        arr = A.split('.')
        if len(arr)>2 or len(arr[-1]) == 0:
            return 0
        elif len(arr) == 2:
            dec = len(arr[0])

        if dec >= exp and dec!=0 and exp!=0:
            return 0

        A = A.replace('.','').replace('e','').replace('-','').replace('+','').replace(' ','')
        if not len(A):
            return 0
        for i in range(len(A)):
            if ord(A[i]) > 57 or ord(A[i])<48:
                res = 0
                break

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.isNumber('1.e1'))
