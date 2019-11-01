import ctypes
import  sys
class DynamicArray(object):

    #init and set 3 attributes
    def __init__(self):
        #element/cell count
        self.n = 0
        # set default capacity
        self.capacity = 1
        # A refs our method to construct an array of our default capacity
        self.A = self.make_array(self.capacity)
    
    def __len__(self):
        #our method to return cell/elemt count per time
        return self.n

    def get_size(self):
        return self.n

    def __getitem__(self, k):

        # if k is not in between 0 and the  current size of the array .ie self.n
        if not 0 <= k <self.n:
            return IndexError('K is out of bounds')
        # if it is between/valid
        #return the element of our array A corresponding to your argument k
        return self.A[k]            

    #public method to add to array/list
    def append(self, element):
        #first check if our current size is same as capacity
        if self.n == self.capacity:
            # use resize method to double up capacity
            self._resize(2*self.capacity)

        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)

        for item in range(self.n):
            B[item] = self.A[item]

        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


# arr = DynamicArray()
# arr.append(1)
# arr.append(5)
# arr.append(3)

# print(len(arr))
# print(sys.getsizeof(arr))
 

arg_array = 10
def caller(arg):
    dyno = DynamicArray()
    for item in range(arg):
        dyno.append(item * 2)
        a = len(dyno)
        d_size = sys.getsizeof(dyno)
        print(dyno[item], dyno.get_size())


    #return dyno

caller(arg_array)
        




class M(object):
    def public(self):
        print("All can see me ")

    def _private_meth(self):
        print('no you cant')
        

# me = M()
# me.public()
# me._private_meth()