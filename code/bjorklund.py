## http://www.atonalmicroshores.com/2014/03/bjorklund-py/
def bjorklund(k, n, r=0):
    """Compute bjorklund's algorithm

    k: number of pulses (negative to reverse)
    n: number of steps (negative to change 0/1 pattern)
    r: shift
    """
    
    A_val = 1
    B_val = 0
    reverse = False
    if k < 0:
        k = abs(k)
        reverse = True
    if n <= 0:
        if n == 0:
            # lazy error handling
            return []
        n = abs(n)
        A_val = 0
        B_val = 1
    ## initialize pattern        
    A = [[A_val]] * k
    B = [[B_val]] * (n-k)
    A_groups = len(A)
    least = min(A_groups, len(B))
    while least > 1:
        for x in range(least):
            A[x] = A[x] + B[x]
        if least == A_groups:
            B = B[least:]
        else:
            A, B = A[:least], A[least:]
        A_groups = len(A)
        least = min(A_groups, len(B))
    output = []
    for group in A:
        output +=  group
    for group in B:
        output += group
    if reverse:
        output.reverse()
    if r != 0:
        output = output[r:] + output[:r]
    return output


assert(bjorklund(2,4) == [1, 0, 1, 0])
assert(bjorklund(5,8) == [1, 0, 1, 1, 0, 1, 1, 0])
assert(bjorklund(5,8,True) == [0, 1, 1, 0, 1, 1, 0, 1])
