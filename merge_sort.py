import random

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = nums[ :mid]
    right = nums[mid: ]

    left_sorted , right_sorted = merge_sort(left) , merge_sort(right)

     
    sorted = merge(left_sorted , right_sorted)
    return sorted


def merge(num1 , num2):
    i , j = 0 , 0 
    merged = []

    while i < len(num1) and j < len(num2):
        if num1[i] <= num2[j]:
            merged.append(num1[i])
            i += 1

        else:
            merged.append(num2[j])
            j += 1

    num1_tile = num1[i:]
    num2_tile = num2[j: ]

    return merged + num1_tile + num2_tile

nums = list(range(1000))
random.shuffle(nums)
result = merge_sort(nums)
print(result)