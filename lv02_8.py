def f08_filter_greater(lst: list[int], n: int) -> list[int]:
    new = []
    for i in lst :
        if lst[i]<= n:
            new.append(lst[i])
    return new
print(f08_filter_greater([0,1,2,3,4,5,6,7],5))