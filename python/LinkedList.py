class Node:

    def __init__(self, value=None, next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class LinkedList:
    data_list = None
    head = None

    def __init__(self):
        self.data_list = None
        self.head = None

    def list_to_ll(self, data):
        self.data_list = data

        l = len(data)

        if not l:
            return None

        ll = []

        for d in data:
            n = Node(d)
            ll.append(n)

        for i in range(l-1):
            ll[i].next = ll[i+1]

        self.head = ll[0]
        return ll[0]

    def ll_to_list(self, head=None):
        if head:
            n = head
        else:
            n = self.head
        a = []
        while n:
            a.append(n)
            n = n.next

        self.node_list = a

    def print_list(self, head=None):
        if head:
            n = head
        else:
            n = self.head
        while n:
            print(n.val)
            n = n.next
