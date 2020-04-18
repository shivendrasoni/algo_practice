# https://www.interviewbit.com/problems/merge-two-sorted-lists/

from algo.LinkedList import LinkedList,Node

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):

        dummy = Node(None)
        curr = dummy
        while A and B:  # choose node with min value from two lists
            if A.val <= B.val:
                curr.next = A
                A = A.next
            else:
                curr.next = B
                B = B.next
            curr = curr.next
        if A:  # list1 is longer, add whatever is left from it
            curr.next = A
        elif B:
            curr.next = B
        return dummy.next


if __name__ == '__main__':
    A = LinkedList()
    A.list_to_ll([1,2,3])

    B = LinkedList()
    B.list_to_ll([4,5,6])

    b = Solution().mergeTwoLists(A.head,B.head)

    LinkedList().print_list(b)


