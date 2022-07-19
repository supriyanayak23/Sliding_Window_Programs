def sumOddLengthSubarrays(arr):
    l = []

    j = 0
    while j < len(arr):
        l.append(arr[j])
        j+=1

    size=3
    while size <= len(arr):
        i,j = 0,0
        sum1 = 0
        while j < len(arr):
            sum1 = sum1 + arr[j]

            if (j-i+1 < size):
                j+=1
                #print(sum1)
            elif (j-i+1 == size):
                print("hi")
                l.append(sum1)
                sum1 = sum1-arr[i]
                i+=1
                j+=1
        size+=2
    print(l)
    return sum(l)

arr = [1,4,2,5,3]
s = sumOddLengthSubarrays(arr)
print(s)

