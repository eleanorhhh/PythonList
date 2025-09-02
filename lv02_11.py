def f11_rotate_right(lst: list, k: int) -> list :
    index = k%(len(lst))
    new = []
    for i in lst[-(index):] :
        new.append(i)
    for i in lst[:-(index)]:
        new.append(i)
    return new
print(f11_rotate_right([1,2,3,4,5,6],10))