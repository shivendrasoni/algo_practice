# https://www.interviewbit.com/problems/partition-list/

from python.LinkedList import LinkedList, Node

class Solution:

    def partition(self, A, B):
        l = Node()
        r = Node()

        h1 = l
        h2 = r
        while A:

            if A.val < B:
                h1.next = A
                h1 = h1.next
            else:
                h2.next = A
                h2 = h2.next

            A = A.next
        h1.next = None
        h2.next = None

        l = l.next
        r = r.next

        h1.next = r

        return l


if __name__ == '__main__':
    ll = LinkedList()
    ll.list_to_ll([6,4,3,2,5,1])
    k =3
    c = Solution().partition(ll.head, k)

    ll.print_list(c)

