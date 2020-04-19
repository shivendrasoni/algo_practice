# https://www.interviewbit.com/problems/rotate-list/
from python.LinkedList import LinkedList

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def length(self,A):
        c = 0

        while(A):
            c +=1
            A = A.next
        return c

    def rotateRight(self, A, B):
        l = self.length(A)

        t1 = A
        r = B % l

        if r == 0:
            return A

        for i in range(l-r-1):
            t1 = t1.next

        t2 = t1.next

        head = t1.next

        while(t2.next):
            t2= t2.next

        t2.next = A
        t1.next = None

        return  head





if __name__ == '__main__':
    ll = LinkedList()
    ll.list_to_ll([1,2,3,4,5])
    k =3
    c = Solution().rotateRight(ll.head, k)

    ll.print_list(c)
