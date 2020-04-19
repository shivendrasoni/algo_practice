# https://www.interviewbit.com/problems/redundant-braces/
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for i in range(len(A)):
            # Dont add anything to stack other than given operators
            if A[i] in '(+-/*':
                stack.append(A[i])
            elif A[i] == ')':
                if stack.pop() == '(':
                    return 1
                stack.pop()
        return 0


if __name__ == '__main__':
    S = '((A+B))'
    print(Solution().braces(S))
