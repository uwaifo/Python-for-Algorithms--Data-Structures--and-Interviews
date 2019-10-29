import timeit
def sum1(n):
    finnal_sum = 0

    for x in range(1,n + 1): # same as for x in range(n + 1)
        print(finnal_sum ,"+", x)
        finnal_sum += x

    return finnal_sum
#print(sum1(10))


def sum_2(n):
    return (n*(n+1))/2


print(sum_2(10))
