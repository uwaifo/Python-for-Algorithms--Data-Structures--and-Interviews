import  sys

n = 10
#store data
data = []

for item in range(n):
    #length od data
    a = len(data)
    #size of data
    b = sys.getsizeof(data)
    print('Lenngth:{0:3d}; Size in bytes: {1:4d} '.format(a,b))

    data.append(item)