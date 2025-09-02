def f12_rle(lst: list) -> list[tuple] :
    new =[]
    index = 1
    for i in range(0,len(lst)-1):
        
        if lst[i] == lst [i+1]:
            index = index+1
        else:
            new.append((lst[i],index))
            index =1
    new.append((lst[len(lst)-1],index))
    return new

print(f12_rle([1,2,2,2,3,3,3,3,3,3,3,4,5,5,5,6,6,6]))