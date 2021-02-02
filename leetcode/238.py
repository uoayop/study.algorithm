from functools import reduce

def productExceptSelf(nums):

    array=[]
    for i in range(len(nums)):

        if i==0:
            left=[]
        else:
            left=nums[:i]

        if i==len(nums)-1:
            right=[]
        else:
            right=nums[i+1:]

        result_array=left+right
        temp_sum = reduce(lambda x,y: x*y, result_array, 1)
        array.append(temp_sum)

    return array

print(productExceptSelf([1,2,3,4]))