def f14_two_sum_all(nums: list[int], target: int) -> list[tuple[int,int]]:
    new = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target and i >j :
                new.append((i,j))
    return new
print(f14_two_sum_all([1,2,3,2],4))