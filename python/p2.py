class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):

        arr = A.split('.')
        brr = B.split('.')
        if len(arr) > len(brr):
            z = len(arr)-len(brr)
            brr = brr+['0']*z
        else :
            z = len(brr)-len(arr)
            arr = arr+['0']*z

        i = 0
        res = 0
        while(i<len(arr)):

            if int(arr[i])>int(brr[i]):
                res = 1
                break
            elif int(arr[i])<int(brr[i]):
                res = -1
                break

            i += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion('13.0', '13.0.8'))
