#交錯合併兩清單
def f05_merge_alternate(a: list, b: list) -> list :
    len_a=len(a)
    len_b=len(b)
    minLen=min(len_a,len_b)
    new = []
    
    for i in range(minLen) :
        new.append(a[i])
        new.append(b[i])
    
    if len_a >minLen:
        new.extend(a[minLen:])
    elif len_b > minLen:
        new.extend(b[minLen:])
    
    return new
print(f05_merge_alternate(['a','b','c'],['a','b','c','v','k']))
