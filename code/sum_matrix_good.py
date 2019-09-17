def sum_matrix(m):
    """given a matrix (stored as a 'rectangular' list of lists),
    return the sum of the elements
    
    input: a rectangular list of lists containing numerical values
    output: a number
    """
    nrows = len(m)
    ncols = len(m[0])
    total = 0
    for i in range(nrows):
        for j in range(ncols):
            total += m[i][j]
    return(total)

# is this file is run directly within the IDE or the Python console
# then the variable __name__ is assigned the value "__main__"".
# if this file is imported by some other file that is then run,
# the value of __name__ assigned to this file will be "sum_matrix_good".
# So, the following code gets executed only if this file is run directly,
# and not first imported.

if __name__ == "__main__":
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[1,2],[3,4],[5,6]]
    print(sum_matrix(m1))
    print(sum_matrix(m2))
