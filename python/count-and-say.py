# https://www.interviewbit.com/problems/count-and-say/
from collections import OrderedDict
class Solution:
    # @param A : integer
    # @return a strings

    def get_seq(self, n):

        ch = n[0]
        co = 1
        ans =''
        for i in range(1, len(n)):
            if ch == n[i]:
                co += 1
            else:
                ans += str(co)+ch
                ch =n[i]
                co =1
        return ans+str(co)+ch

    def countAndSay(self, A):

        if A==0:
            return '0'
        elif A==1:
            return '1'

        ans = '1'

        while A>1:
            ans = self.get_seq(ans)
            A -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))
