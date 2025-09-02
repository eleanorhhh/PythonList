def f10_local_peaks(nums: list[int]) -> list[int]:
    index = []
    for i in range(1,len(nums)-1):
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            index.append(nums[i])
    return index

print(f10_local_peaks([1,2,1,4,5,3]))