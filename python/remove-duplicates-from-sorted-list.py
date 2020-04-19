# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
from python.LinkedList import LinkedList

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        B = Node(None)

        while A.next:

            if (A.val == A.next.val):
                B = A.next.next
                A.next = B

            else:
                A = A.next

        return head


if __name__ == '__main__':
    ll = LinkedList()
    ll.list_to_ll([1,1,2,2,2,2,3,5,5])

    s1 = Solution()
    head = s1.deleteDuplicates(ll.head)
    ll.print_list()
