numlist = [2,1,1,4,1,2,4,6,8,9,3,5,7,5]

def bubble_stl(nums):
    end = len(nums)-1
    while end >= 0:
        swapped = -1
        for i in range(0, end):
            if nums[i] > nums[i+1]:
                j = i + 1
                nums[i], nums[j] = nums[j], nums[i]
                swapped = i
        end = swapped

    return nums

print(bubble_stl(numlist))
