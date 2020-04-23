def load_balance(arr ) -> bool:

    i = 1
    j = len(arr)-1


    sum_left = arr[0]

    sum_right = arr[len(arr)-1]



    while(i<j):

        if sum_left > sum_right:
            sum_right += arr[j]
            j -= 1
        elif sum_left < sum_right:
            sum_left += arr[i]
            i += 1
        else:
            sum_left += arr[i]
            i+=1
            sum_right += arr[j]
            j -= 1

    if i<j:
        mid_sum = sum(arr[i+1: j])

        if mid_sum == sum_left and mid_sum == sum_right:
            return True
    else:
        return False
if __name__ == '__main__':


    # print(load_balance([1,3,4,2,2,2,1,1,2]))
    print(load_balance([1,1,1,1,1,1,1,1]))
