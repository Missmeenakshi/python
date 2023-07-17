
def sort(nums):
    for i in range(6):
        minpos = i
        for j in range (i, 7):
            if nums[j] < nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)

nums = [8, 9, 4, 3, 7, 5, 1]
sort(nums)
print(nums)
