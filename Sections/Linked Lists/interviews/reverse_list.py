class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        
def reverse(head):
    previous = None
    current = head
    while current:
        temp_next = current.nextnode
        current.nextnode = previous
        previous = current
        current =temp_next
    head = previous
    #return
 

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

reverse(a)
#print(d.nextnode.value)
    