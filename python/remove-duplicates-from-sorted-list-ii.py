# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/

from python.LinkedList import LinkedList

class Solution:
    def deleteDuplicates(self, A):

        b = Node()
        b.next = A
        prev = b
        curr = A
        while(curr):

            while curr.next and curr.next.val == prev.next.val:
                curr = curr.next

            if prev.next == curr:
                prev = prev.next
            else:
                prev.next = curr.next

            curr = curr.next

        return b.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.list_to_ll([7,8,8,9,9,10,11,11,11])

    b = Solution().deleteDuplicates(ll.head)

    ll.print_list(b)

