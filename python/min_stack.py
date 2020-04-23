class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if self.min_stack and self.min_stack[-1] > x:
            self.min_stack.append(x)
        elif not self.min_stack:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if self.min_stack and self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        if self.stack:
            self.stack.pop()


    # @return an integer
    def top(self):
        return self.stack[-1] if self.stack else -1

    # @return an integer
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else -1



if __name__ == '__main__':
    stak = MinStack()
    # Line 1 ( Corresponds to arg 1 ) : The line starts with a number numOperations, corresponding to the number of operations.
    # Then "numOperation" operations follow.
    # Each operation is either :
    # * P <number> : Corresponds to push(<number>) in stack
    # * p : Corresponds to pop()
    # * t : Corresponds to top()
    # * g : Corresponds to getMin() call.
    # Note that the function calls are made in order.

    inp = '19 P 10 P 9 g P 8 g P 7 g P 6 g p g p g p g p g p g'
    arr = inp.split(' ')
    num_operations = arr[0] # Dont need this though.

    i = 0

    while(i<len(arr)):

        if arr[i] == 'p':
            stak.pop()
        elif arr[i] == 'g':
            print(stak.getMin())
        elif arr[i] == 't':
            print(stak.top())
        elif arr[i] == 'P':
            stak.push(int(arr[i+1]))

        i += 1

