def sum_matrix(m):
    """given a matrix (stored as a 'rectangular' list of lists),
    return the sum of the elements
    """
    nrows = len(m)
    ncols = len(m[0])
    i = 0
    j = 0
    total = 0
    while i<nrows:
        while j<ncols:
            total += m[i][j]
        i += 1
    return(total)

if __name__ == "__main__":
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[1,2],[3,4],[5,6]]
    print(sum_matrix(m1))
    print(sum_matrix(m2))
