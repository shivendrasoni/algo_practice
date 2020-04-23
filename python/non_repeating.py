# input: [1,1,4,4,7,8,8]
# output: 7

# In a sorted array, find teh non repeating element. Other elements repeat only once.
def non_repeating(A):

    l = 0
    h = len(A)-1

    while(l<h):
        mid = l + (h-l)//2

        if mid%2:
            if A[mid] == A[mid-1]:
                l = mid+1
            else:
                h = mid -1

        else:
            if A[mid] == A[mid+1]:
                l = mid+2
            else:
                h = mid

    return A[l]

if __name__ == '__main__':
    print(non_repeating([1,1,4,4,8,8, 9]))
