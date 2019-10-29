'''
Note this is tricky, but x is cut in half each time through the loop, so it will only take log(n) iterations! Refer to the HW reading assignment for more info!
'''
def tester(n):
    x = n
    while x > 0:
       y = 2 + 2
       x = x # 2
    return x


#Complexity = 0(Log(n))

##print(tester(4))


def insignificat(n):
    print(n)
    w = 0
    for x in range(n):
        w = w + 1
     
    for y in range(n):
        w = w - 1
    return w
        

#Complexity = O(n)
# here we disregard the insignificant subtracting step that would have been O(2n)
print(insignificat(5))
