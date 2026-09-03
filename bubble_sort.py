def bubble_sort(nums):

    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] >= nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]

    print(nums)   
nums = [2,6,3,9,5,3,5]
bubble_sort(nums)        