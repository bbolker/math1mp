def ascend_fun(numbers):
    is_ascending = True
    n = len(numbers)
    i = 0
    while i<(n-1):
        if numbers[i+1]<numbers[i]:
            is_ascending = False
        i += 1
    return(is_ascending)

if __name__ == "__main__":
    print(ascend_fun([0,1,2,3,4]))
    print(ascend_fun([]))
    print(ascend_fun([0,1]))
    print(not ascend_fun([1,0]))
