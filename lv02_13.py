def f13_prefix_sums(nums: list[int]) -> list[int]:
    sum = 0
    new = []
    for i in range(len(nums)):
        sum = sum+nums[i] 
        new.append(sum)
    return new
print(f13_prefix_sums([1,2,3,4,5,6]))