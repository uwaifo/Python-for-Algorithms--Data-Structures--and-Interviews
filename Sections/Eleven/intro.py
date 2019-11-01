'''
Commonly called array sequnces
There three main sequence classes, namely:
1.List : [1,2,3]
2.Tuple : (1,2,3)
3.String : '123'
And they all support indexing
'''

my_string = '123'
my_tuple =(1,2,3)
print(my_string[0])
print(my_tuple[0])

'''
memory is made of bits
unit of 8 bits is a byte

Python stores each Unicode character with 16bits (2 bytes)
Therefore the string 'hello' would be stored in 10bits(5 bytes) of memory
the location of storage is the memerry address

STUDY
Deep copy
Shallow copy
'''
#Referential Array
array = ['jimmy', 'idehenre', 'inegbenehinehiagbeme']
#Python array elements/cells are actually fixed is size. 
#Here each cell references other memory address to store string values while they 
#just hold there references

print('Referential Arrays')
# Bellow all 8 cells are referencing the same object that store the value of 0
counter = [0]*8 

print(counter)

print('Extending Arrays')
#like reference the extending array thoug it grow in size will only have the new cells refence the 
#object space ocupied by the previous . 
#
l1 = [1,2,3,4,5]
l2 = [6,7,8]
l1.extend(l2)
print(l1)
#thus l2 still exists
print(l2)

