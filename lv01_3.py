#最大/最小/總和/平均 
def f03_max_min_sum_avg(lst: list[float]) -> tuple[float,float,float,float] :
    
    return max(lst),min(lst),sum(lst),sum(lst)/len(lst)

print(f03_max_min_sum_avg([10,11,12,13,14,15]))
