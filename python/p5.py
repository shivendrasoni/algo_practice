# https://www.interviewbit.com/problems/3-sum-zero/

class Solution:
    # @param A : list of integers
    def threeSum(self, A):
        A = sorted(A)
        diff = 99999999
        res = set()
        i,j,k = 0,1,len(A)-1
        l = len(A)-2

        while(i<l):
            j=i+1
            k = l+1
            while(j<k):
                sum1 = A[i]+A[j]+A[k]
                if (0 == sum1):
                    res.add((A[i],A[j], A[k]))
                if(sum1 < 0):
                    j+=1
                else:
                    k-=1

            i+=1
        return list(res)


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0 ,1, 2, -1,-4]))


