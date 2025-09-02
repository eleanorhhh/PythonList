def f06_flatten_2d(matrix: list[list]) -> list :
    new = []
    for row in matrix:
        for i in row:
            new.append(i)
    return new
print(f06_flatten_2d([[1,2,3,4],[5,6,7],[8,0]]))