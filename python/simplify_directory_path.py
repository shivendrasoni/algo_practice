# https://www.interviewbit.com/problems/simplify-directory-path/

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):

        A = A.strip('/')
        arr = A.split('/')

        stack = []
        for c in arr:
            if c == '/' or c == '.' or c =='':
                continue
            elif c == '..' and stack:
                stack.pop()
            elif c == '..' and not stack:
                continue
            else:
                stack.append(c)

        res = '/'.join(stack)
        return '/'+res
