def f07_to_ints(strs: list[str]) -> list[int]:
    new = []
    for i in strs:
        try:
            new.append(int(i))
        except ValueError:
            pass
    return new
print(f07_to_ints([0.1,13,10.2,'app',7.88]))