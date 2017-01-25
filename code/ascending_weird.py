def ascend_fun_weird(numbers):
    n = len(numbers)
    for i in range(0,n+1):
        curval = numbers[i:i+1]
        nextval = numbers[i+1:i+2]
        if curval <= nextval:
            is_ascending = True
        else:
            is_ascending = False
            break

if __name__ == "__main__":
    print(ascend_fun([0,1,2,3,4]))
    print(ascend_fun([]))
    print(ascend_fun([0,1]))
    print(not ascend_fun([1,0]))
