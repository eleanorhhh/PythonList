def f09_squares(n: int) -> list[int] :
    new = []
    if n>=1:
        for i in range(n):
            new.append(pow(i+1,2))
    else:
        return 'error'
    return new
print(f09_squares(10))