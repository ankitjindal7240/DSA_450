arr=[3,0,5,2,0,4]
def rainWater(arr):
    # max height building in left
    left_max= []
    left_max.append(arr[0])
    for i in range(1,len(arr)):
        if left_max[i-1]>arr[i]:
            left_max.append(left_max[-1])
        else:left_max.append(arr[i])

    # max height building in right
    right_max=[]
    right_max.append(arr[-1])
    for i in reversed(range(len(arr)-1)):
        if right_max[-1]>arr[i]:
            right_max.append(right_max[-1])
        else:
            right_max.append(arr[i])
    right_max=right_max[::-1]
    print(left_max,right_max)

    # find min from both side and find diff between array element and heght i.e. water stored by building and add it to aswer
    ans=0
    for i in range(len(arr)):
        max_height=min(right_max[i],left_max[i])  # check min of both max
        water= max_height-arr[i]
        ans=ans+water
