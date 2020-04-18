# https://www.interviewbit.com/problems/palindrome-list/
from algo.LinkedList import LinkedList


class Solution:
    def lPalin(self, A):
        slow = A
        fast = A
        prev_of_slow= None

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

        curr = slow
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
            if first.val != second.val:
                return 0
            first = first.next
            second = second.next

        return 1





if __name__ == '__main__':
    ll = LinkedList()
    ll.list_to_ll([1,2,3,4,3,2,1])

    s1 = Solution()
    print(s1.lPalin(ll.head))
    # ll2 = LinkedList()
    # ll2.list_to_ll([1,2,3,4,3,2,1])
    # ll.print_list()
