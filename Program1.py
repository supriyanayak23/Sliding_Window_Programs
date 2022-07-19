def maxsum_SW(arr,k):
    max_sum = -1
    summ = 0
    i,j = 0,0
    #l = []
    while(j < len(arr)):
        summ = summ + arr[j]
        if (j-i+1 < k):
            j+=1
        elif (j-i+1 == k):
            max_sum = max(max_sum,summ)
            #l.append(max_sum)
            summ = summ-arr[i]
            i+=1
            j+=1
    return max_sum

arr = [2,5,1,8,2,2,9,5]
k = 3
res = maxsum_SW(arr,k)
print("Maximum sum of the subarrays of size 3 are:",res)



