# https://www.interviewbit.com/problems/evaluate-expression/
class Solution:
    # @param A : list of strings
    # @return an integer

    def calc_value(self, a,b, op):
        pass
    def evalRPN(self, A):

        if len(A) == 1:
            return A[0]

        if len(A) == 2:
            return A[0]
        while A:
            if A[-1] in '+-/*':
                op = A[-1]
                A.pop()
            b = A[-1]
            if b in '+-/*':
                b= self.evalRPN(A)
            A.pop()
            a = A[-1]
            if a in '+-/*':
                a= self.evalRPN(A)

            res = eval(str(a)+op+str(b))

            return int(res)



if __name__ == '__main__':

    S = ["2"]
    print(Solution().evalRPN(S))
