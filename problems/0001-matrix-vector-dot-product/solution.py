# Cell 1
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if not a or not a[0]:
        return -1
    
    num_cols= len(a[0])
    if len(b) != num_cols:
        return -1
    
    results= []
    for row in a :
        if num_cols != len(row):
            return -1
        row_dot= sum(x*y for x,y in zip(row,b))
        results.append(row_dot)
    return results