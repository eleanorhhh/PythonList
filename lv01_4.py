#去重且保留原順序
def f04_unique_keep_order(lst: list) -> list :
    seen = []
    for i in lst:
        if i  not in  seen:
            seen.append(i)
            
    return seen

print(f04_unique_keep_order(['a','b','c','b','f','e']))
