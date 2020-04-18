# https://www.interviewbit.com/problems/subtract/

from algo.LinkedList import LinkedList,Node

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverse_linked_list(self, A):
        curr = A
        fut = None
        prev = None

        while(curr):
            fut = curr.next
            curr.next = prev
            prev = curr
            curr = fut

        return curr

    def subtract(self, A):
        slow = A
        fast = A
        prev_of_slow = None

        while(fast and fast.next):
            prev_of_slow = slow
            slow = slow.next
            fast = fast.next.next

        if fast == None:
            # Even numbered list
            prev_of_slow = None #break list
        else:
            # if list is odd : ignore the middle element
            if prev_of_slow is not None:
                prev_of_slow.next = None
            slow = slow.next

        #         reverse the second half of list

        curr = self.reverse_linked_list(slow)
        fut = None
        prev = None

        while(curr):
            fut = curr.next
            curr.next = prev
            prev = curr
            curr = fut

        first = A
        second = prev

        while first and second:
            first.val = second.val-first.val
            first = first.next
            second = second.next

        while first.next:
            print(first.val)
            first = first.next

        first.next = second
        return A


if __name__ == '__main__':
    ll = LinkedList()
    ll.list_to_ll([ 95,59,26,16,31,39,29,8,74,14,41,41,64,88,34,21,67,23,17,41,3,38,4,45,93,92,99,24])

    s1 = Solution()
    h = s1.subtract(ll.head)

    LinkedList().print_list(head=h)
